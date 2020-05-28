import os
from PIL import Image

dir_path = "D:\\Civ6Mod\\2D\\LeaderPortrait\\Resize_Bulk_Test"

sizes = [32, 45, 50, 55, 64, 80, 256]

for file in os.listdir(dir_path):
    fullpath = dir_path + "\\" + str(file)
    for size in sizes:
        image = Image.open(fullpath).convert("RGBA")
        image = image.resize((size, size), Image.ANTIALIAS)
        image.save(fullpath.replace("256.png", str(size) + ".png"))
