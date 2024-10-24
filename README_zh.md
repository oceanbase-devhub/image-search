# 图像搜索应用

## 介绍

凭借 OceanBase 的向量存储和检索能力，我们可以构建一个图像搜索应用。该应用会把图像嵌入为向量中并存储在数据库中。用户可以上传图像，应用程序将搜索并返回数据库中最相似的图像。

注意：您需要自己在准备一些图像并将 `Image Base` 配置更新到打开的 UI 中。如果您本地没有可用的图像，可以在线下载数据集，例如在 Kaggle 上的 [Animals-10](https://www.kaggle.com/datasets/alessiocorrado99/animals10/data) 数据集。

## 准备工作

1. 安装 [Python 3.9](https://www.python.org/downloads/) 及以上版本及对应的 [Pip](https://pip.pypa.io/en/stable/installation/) 工具

2. 安装 [Poetry](https://python-poetry.org/docs/) 作为依赖管理工具，可参考下面的命令

```bash
python3 -m pip install poetry
```

## 应用搭建步骤

### 1. 安装依赖

```bash
# 安装依赖
poetry install
```

### 2. 启动图像搜索 UI

```bash
# 启动图像搜索应用界面
poetry run streamlit run --server.runOnSave false image_search_ui.py
```

### 3. 处理并存储图像数据

打开应用界面之后，您可以在左侧侧边栏中看到“图片加载目录”的输入框，在其中填写您准备的图片目录的绝对路径，然后点击“加载图片”按钮。应用程序将处理并存储这些图像数据，您将在界面上看到图片处理进度。

### 4. 使用图像搜索

在图片处理完成后，您将在界面中上方看到图片上传操作栏，您可上传一张图片用于搜索相似图片。上传图片后，应用程序将搜索并返回数据库中最相似的一些图片，默认返回最相似的前 10 张图片。

![image_search_ui](./demo/image-search-demo.png)

## 常见问题

### 1. 遇到找不到 libGL.so.1 文件的报错怎么办？

如果您在运行应用 UI 时遇到了 `ImportError: libGL.so.1: cannot open shared object file` 的报错信息，可参考[该帖子](https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo)解决。

在 CentOS 操作系统中，执行以下命令,

```bash
sudo yum install mesa-libGL -y
```

在 Ubuntu/Debian 操作系统中，执行以下命令,

```bash
sudo apt-get install libgl1
```

### 2. 遇到找不到 pkg_resources 包的报错怎么办？

如果您在运行应用 UI 时遇到了 `ModuleNotFoundError: No module named 'pkg_resources'` 的报错信息，可参考[该帖子](https://stackoverflow.com/questions/7446187/no-module-named-pkg-resources)解决。

具体来说，可以参考下面两条命令，

```bash
python3 -m pip install --upgrade pip
python3 -m pip install setuptools
```
