import xml.etree.ElementTree as ET

xml = ET.parse("D:\\Civ6Mod\\gitproject\\CWON_Burj_Khalifa\\CWON_Burj_Khalifa\\Assets\\Burj_Khalifa_Wonder.ast")

root = xml.getroot()

for child in root:
    if child.tag == 'm_BehaviorData':
        for child2 in child:
            if child2.tag == 'm_behaviorDataSets':
                for child3 in child2:
                    if child3.tag == 'm_attachmentPoints':
                        for child4 in child3:
                            for child5 in child4:
                                name = ""
                                xpos = ""
                                ypos = ""
                                zrot = ""
                                scale = ""
                                for child6 in child5:
                                    if child6.tag == 'm_Name':
                                        name = child6.attrib['text']
                                    if child6.tag == 'm_scale':
                                        scale = child6.text
                                    if child6.tag == 'm_position':
                                        for child7 in child6:
                                            if child7.tag == 'x':
                                                xpos = child7.text
                                            if child7.tag == 'y':
                                                ypos = child7.text
                                    if child6.tag == 'm_orientation':
                                        for child7 in child6:
                                            if child7.tag == 'z':
                                                zrot = child7.text

                                print ("("+",".join(["'"+name+"'", xpos, ypos, zrot, scale])+"),")