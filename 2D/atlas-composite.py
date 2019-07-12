from PIL import Image

import os

dir_path = "D:\\mod\\Artifacts_and_Relics\\Artifact_Relics_Images\\atlas"

directory = os.fsencode(dir_path)

dims = (2048, 2048)

out_image = Image.new('RGBA', dims, (0, 0, 0, 0))

for file in os.listdir(directory):

    full_filename = dir_path + '\\' + os.fsdecode(file)
    print(full_filename)

    out_image = Image.alpha_composite(out_image, Image.open(full_filename))

out_image.save("D:\\mod\\Artifacts_and_Relics\\Artifact_Relics_Images\\atlas\\atlas.png")