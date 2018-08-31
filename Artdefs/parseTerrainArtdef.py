import xml.etree.ElementTree as ET
import os

materials = []

for path, subdirs, files in os.walk("D:\\mod\\Terrain\\Materials"):
    for name in files:
        xml = ET.parse(path+"\\"+name)
        root = xml.getroot()
        for child in root:
            if child.tag == 'm_CookParams':
                for values in child:
                    for value in values:
                        if value.get('class') == 'AssetObjects..RGBValue':
                            r, g, b = 0.0, 0.0, 0.0
                            for rgb in value:
                                if (rgb.tag == 'm_r'):
                                    r = float(rgb.text)
                                if (rgb.tag == 'm_g'):
                                    g = float(rgb.text)
                                if (rgb.tag == 'm_b'):
                                    b = float(rgb.text)
                        if value.get('class') == 'AssetObjects..FloatValue':
                            a = 0.0
                            for rgb in value:
                                if (rgb.tag == 'm_fValue'):
                                    a = float(rgb.text)
        materials.append((name, r, g, b, a))

for material in materials:
    print("%s,%.0f,%.0f,%.0f,%.0f" % material)