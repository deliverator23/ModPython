from PIL import Image

import os
from pathlib import Path

texture_filename = "darius_skin_norm_1024.dds"

dir_path = "C:\\Users\\User\\Documents\\My Games\\Sid Meier's Civilization 5\\ScreenShots"

paths = sorted(Path(dir_path).iterdir(), key=os.path.getmtime)

image_path = paths[-1:][0]

image = Image.open(image_path).convert("RGB")
image = image.crop((445, 21, 1469, 1045))
png_filename = str(image_path).replace(".tga", ".png")
image.save("D:\\Civ5Mod\\Leaderhead_Work\\HQ_Textures\\" + texture_filename.replace(".dds",".png"))
print(image.size)