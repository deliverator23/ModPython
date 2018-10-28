import xml.etree.ElementTree as ET
import os

models_path = "D:\\Civ6Mod\\Civ5Unpacks\\UnitConversionsPart2\\"

with open(models_path + "\\civ5units2.dat", 'w') as f:

    for path, subdirs, files in os.walk(models_path):
        for filename in files:
            if filename.endswith(".fxsxml"): # and filename.startswith("aegis"):
                mesh = ""
                animations = []
                textures = []
                xml = ET.parse("%s%s" % (models_path,filename))
                root = xml.getroot()
                for child in root:
                    if (child.tag == "Mesh"):
                        mesh = child.attrib["file"]
                    if (child.tag == "Animation"):
                        animations.append(child.attrib["file"])
                    if (child.tag == "Texture"):
                        textures.append(child.attrib["file"])

                animationsString = ",".join(v for v in animations)
                texturesString = ",".join(v for v in textures)
                print("%s;%s;%s;" % (mesh, animationsString, texturesString ),file=f)