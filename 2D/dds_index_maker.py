import os
from PIL import Image
import os

dir_path = "D:\\Civ5Mod\\Leaderhead_Work\\Expansion1Leaders\\resaveBatch\\Modbuddy\\Textures"

dds_files = []

dds_images = []

for file in os.listdir(dir_path):
    filename = str(file).lower()

    if filename.endswith(".dds"):
        fullpath = dir_path + "\\" + filename
        image = Image.open(fullpath).convert("RGBA")

        dims = image.size

        record = (filename, dims[0], dims[1])
        dds_images.append(record)


dds_images = sorted(dds_images, key=lambda x: x[1], reverse=True)

for image in dds_images:
    print(image[1], "x", image[2], ";", image[0])