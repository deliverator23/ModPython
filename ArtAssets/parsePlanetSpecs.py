import os
import xml.etree.ElementTree as ET


biomes = ["Arid","Frigid","Fungal","Lush","Primordial"]

overDict = {}

planetSpecsPath = "D:\\SteamLibrary\\steamapps\\common\\Beyond Earth - Rising Tide Demo\\assets\\PlanetSpec\\"
for path, subdirs, files in os.walk(planetSpecsPath):
    for filename in files:
        if filename.endswith("_Overrides.xml"):  # and filename.startswith("aegis"):
            readfilename = "%s%s" % (planetSpecsPath, filename)
            #print(readfilename)
            xml = ET.parse(readfilename)
            root = xml.getroot()
            for override in root:
                if (override.tag == "Textures"):
                    for texture in override:
                        origTex = texture.attrib["Original"]
                        overTex = texture.attrib["Override"]
                        if ("DIFF" in origTex.upper()):
                            #print("%s %s" % (origTex, overTex))
                            if not origTex in overDict:
                                overDict[origTex] = [overTex]
                            else:
                                if not overTex in overDict[origTex]:
                                    overDict[origTex].append(overTex)

with open('D:\\mod\\BeyondEarthUnpacks\\UnitModels\\resaveBatch\\unit_models_planets.dat', 'w') as o:
    with open('D:\\mod\\BeyondEarthUnpacks\\UnitModels\\resaveBatch\\unit_models.dat','r') as f:
        for x in f:
            bits = x.split(';')
            assetName = bits[0].replace(".gr2","")
            if len(bits[3].rstrip()) > 0:
                assetName = bits[3].rstrip()

            textureString = bits[2]

            textureNames = textureString.split(',')

            for biome in biomes:
                isOverrideAsset = False
                for textureName in textureNames:
                    if textureName in overDict.keys():
                        for overTextureName in overDict[textureName]:
                            if (biome in overTextureName):
                                isOverrideAsset = True
                                break
                    if isOverrideAsset:
                        break

                if isOverrideAsset:
                    newTextureNames = []

                    for textureName in textureNames:
                        if textureName in overDict.keys():
                            for overTextureName in overDict[textureName]:
                                if (biome in overTextureName):
                                    newTextureNames.append(overTextureName)
                                    break
                        else:
                            newTextureNames.append(textureName)

                    newTextureString = ",".join(v for v in newTextureNames)
                    newAssetName = assetName + "_" + biome
                    geoString = bits[0]
                    animString = bits[1]
                    print("%s;%s;%s;%s" % (geoString,animString, newTextureString, newAssetName), file=o)

        #modelConvDatLines[keyName] = x