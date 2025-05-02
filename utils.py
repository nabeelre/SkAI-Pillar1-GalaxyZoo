import matplotlib.pyplot as plt
from PIL import Image
import os


def show_image_by_assetid(asset_id, images_dir="data/3565489/images/"):
    file_path = os.path.join(images_dir, f"{asset_id}.jpg")
    if os.path.exists(file_path):
        img = Image.open(file_path)

        plt.imshow(img)
        plt.axis('off')
        plt.show()
    else:
        print(f"File not found: {file_path}")
