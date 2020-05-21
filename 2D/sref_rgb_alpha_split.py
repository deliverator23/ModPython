import os
from PIL import Image
import os


dir_path = "D:\\Civ5Mod\\Leaderhead_Work\\Expansion2Leaders\\resaveBatch\\Modbuddy\\Textures"

dds_files = []

for file in os.listdir(dir_path):
    filename = str(file).lower()



    if filename.endswith("sref.dds"):
        fullpath = dir_path + "\\" + filename
        image = Image.open(fullpath).convert("RGBA")

        #g, r, a, b = image.split()
        a, b, g, r = image.split()
        im_rgb = Image.merge('RGB', (r, g, b))

        sref_path = dir_path + "\\sref_alpha\\"
        if not os.path.exists(sref_path):
            os.makedirs(sref_path)

        im_rgb.save(sref_path + filename.replace(".dds", "_rgb.png"))
        a.save(sref_path +  filename.replace(".dds","_alpha.png"))

        #c2.save(fullpath.replace(".dds", "_c2.png"))
        #c3.save(fullpath.replace(".dds", "_c3.png"))
        #c4.save(fullpath.replace(".dds", "_c4.png"))