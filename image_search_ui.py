import os
import time
import dotenv

dotenv.load_dotenv()

import streamlit as st
from image_store import OBImageStore
from connection import connection_args


table_name = os.getenv("IMG_TABLE_NAME", "image_search")
tmp_path = "tmp/temp.jpg"


st.set_page_config(
    layout="wide",
    page_title="图像搜索应用",
    page_icon="demo/ob-icon.png",
)
st.title("🔍 图像搜索应用")
st.caption("🚀 基于 OceanBase 向量检索能力构建的相似图像搜索应用")

with st.sidebar:
    st.title("🔧 应用设置")
    st.logo("demo/logo.png")
    st.subheader("图片搜索设置")
    table_name = st.text_input("表名", table_name)
    top_k = st.slider("召回数量", 1, 30, 10, help="需要返回多少张相似图片")
    show_distance = st.checkbox("显示距离", value=True)
    show_file_path = st.checkbox("显示文件路径", value=True)

    st.subheader("图片加载设置")
    image_base = st.text_input(
        "图片加载目录",
        os.getenv("IMG_BASE", None),
        help="需要加载的存放图片的目录",
        placeholder="图片目录的绝对路径，如 /data/imgs",
    )
    click_load = st.button("加载图片")


store = OBImageStore(
    uri=f"{connection_args['host']}:{connection_args['port']}",
    **connection_args,
    table_name=table_name,
)

table_exist = store.client.check_table_exists(table_name)
if not table_name or table_name.isspace():
    st.error("请设置表名")
    st.stop()
elif click_load:
    if image_base is None:
        st.error("请设置图片加载目录")
    elif not os.path.exists(image_base):
        st.error(f"您设置的图片加载目录 {image_base} 不存在")
    else:
        total = 0
        for _, _, files in os.walk(image_base):
            total += len(files)
        finished = 0
        bar = st.progress(0, text="加载图片中...")
        for _ in store.load_image_dir(image_base):
            finished += 1
            bar.progress(
                finished / total,
                text=f"加载图片中... (已完成 {finished} / {total})",
            )
        st.toast("所有图片加载完成.", icon="🎉")
        st.balloons()
        time.sleep(2)

        st.rerun()
elif table_exist:
    uploaded_file = st.file_uploader(
        label="选择一张图片...",
        type=["jpg", "jpeg", "png"],
        help="上传一张图片进行相似图片搜索",
    )
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        col1.subheader("上传图片")
        col1.caption("📌 您上传的图片")
        col1.image(uploaded_file, use_column_width=True)

        with open(tmp_path, "wb") as f:
            f.write(uploaded_file.read())

        col2.subheader("相似图片")
        results = store.search(tmp_path, limit=top_k)
        with col2:
            if len(results) == 0:
                st.warning("没有找到相似图片")
            else:
                tabs = st.tabs([f"图片 {i+1}" for i in range(len(results))])
                for res, tab in zip(results, tabs):
                    with tab:
                        if show_distance:
                            st.write(f"📏 距离: {res['distance']:.8f}")
                        if show_file_path:
                            st.write("📂 文件路径:", os.path.join(res["file_path"]))
                        st.image(res["file_path"])
else:
    st.warning("图片表不存在，请先加载图片")
