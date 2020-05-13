from PIL import Image

import os
from pathlib import Path
import ntpath

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

texture_filename = "gajah_hair_diff.dds"

dir_path = "C:\\Users\\User\\Documents\\My Games\\Sid Meier's Civilization 5\\ScreenShots"
temp_path = "D:\\temp"

paths = sorted(Path(dir_path).iterdir(), key=os.path.getmtime)

last_four_screenshots = paths[-4:]

z = 1

images = []

for image_path in last_four_screenshots:
    image = Image.open(image_path).convert("RGB")
    image = image.crop((445, 21, 1469, 1045))
    png_filename = temp_path + "\\" + str(ntpath.basename(image_path)).replace(".tga", ".png")
    image.save(png_filename)
    print(image_path, image.size)
    images.append(image)

row1 = get_concat_h(images[0], images[1])
row2 = get_concat_h(images[2], images[3])

row1.save(temp_path + "\\" + "temp_row1.png")
row2.save(temp_path + "\\" + "temp_row2.png")

full_image = get_concat_v(row1, row2)

full_image.save("D:\\Civ5Mod\\Leaderhead_Work\\HQ_Textures\\" + texture_filename.replace(".dds",".png"))

