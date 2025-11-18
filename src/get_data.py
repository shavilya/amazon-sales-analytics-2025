# Importing required libraries for extracting the datasets.

from kaggle import api 
import os

target_dir = os.path.join(os.getcwd(), 'Data', 'raw')

os.makedirs(target_dir, exist_ok=True)

path = api.dataset_download_files(
    "anandshaw2001/amazon-product-sales-2025", 
    path=target_dir , 
    unzip = True
)

print("Path to dataset files:", path) 