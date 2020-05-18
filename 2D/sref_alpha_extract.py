import os
from PIL import Image

dir_path = "D:\\Civ5Mod\\Leaderhead_Work\\Expansion1Leaders\\resaveBatch\\Modbuddy\\Textures"

dds_files = []

for file in os.listdir(dir_path):
    filename = str(file).lower()

    if filename.endswith(".dds"):
        image = Image.open(dir_path + "\\" + filename).convert("RGBA")
        dims = image.size

        file_rec = (filename, dims[0], dims[1], image)
        dds_files.append(file_rec)

dds_files = sorted(dds_files, key = lambda x: (-x[1], x[0]))

counter = 1
prev_x = dds_files[0][1]

for dds_file in dds_files:

    dims_str = str(dds_file[1]) + " x " + str(dds_file[2]) + ";"

    if dds_file[1] != prev_x:
        counter = 1

    print(str(counter) + ":", dims_str, dds_file[0])

    if dds_file[0].endswith("sref.dds"):
        alpha = dds_file[3].split()[-1]
        alpha.save(dir_path + "\\sref_alpha\\" + dds_file[0].replace(".dds", "_alpha.png"))

    prev_x = dds_file[1]
    counter += 1
