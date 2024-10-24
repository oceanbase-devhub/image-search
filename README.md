# Image Search Application

## Introduction

With vector storage and retrieval ability of OceanBase, we can build an image search application. The application will embed the images into vectors and store them in the database. The user can upload an image and the application will search and return the most similar images in the database.

Notes: You need to prepare some images in a folder yourself and update the `Image Base` configuration in opened UI. If you don't have available images locally, you can download a dataset online like [Animals-10](https://www.kaggle.com/datasets/alessiocorrado99/animals10/data) on Kaggle.

```bash
# Install the dependencies for the image search application
poetry install

# Start the image search UI. (You don't need to wait for the entire embedding process to finish)
poetry run streamlit run --server.runOnSave false image_search_ui.py
```
