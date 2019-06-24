import xml.etree.ElementTree as ET

xml = ET.parse("D:\\Civ6Mod\\gitproject\\CWON_Borobudur\\CWON_Borobudur\\Assets\\Borobudur_WonderMovie.ast")

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
                                zpos = ""
                                zrot = ""
                                scale = ""
                                bone_name = ""
                                model_name = ""
                                for child6 in child5:
                                    #print(child6.tag)
                                    #if child6 == 'm_CookParams':
                                    # if child6 == 'm_position':
                                    # if child6 == 'm_orientation':
                                    # if child6 == 'm_Name':
                                    # if child6 == 'm_BoneName':
                                    # if child6 == 'm_ModelInstanceName':
                                    if child6.tag == 'm_position':
                                        #print(child6.tag)
                                        for child7 in child6:
                                            #print(child7.tag, child7.text)
                                            if child7.tag == 'x':
                                                xpos = child7.text
                                            if child7.tag == 'y':
                                                ypos = child7.text
                                            if child7.tag == 'z':
                                                zpos = child7.text

                                    if child6.tag == 'm_orientation':
                                        #print(child6.tag)
                                        for child7 in child6:
                                            #print(child7.tag, child7.text)
                                            if child7.tag == 'z':
                                                zrot = child7.text

                                    if child6.tag == 'm_scale':
                                        #print(child6.tag, child6.text)
                                        scale = child6.text

                                    if child6.tag == 'm_Name':
                                        #print(child6.tag, child6.text)
                                        name = child6.attrib['text']

                                    if child6.tag == 'm_BoneName':
                                        # print(child6.tag, child6.text)
                                        bone_name = child6.attrib['text']

                                    if child6.tag == 'm_ModelInstanceName':
                                        # print(child6.tag, child6.text)
                                        model_name = child6.attrib['text']

                                print("(" + ",".join(["'"+name+"'", "'"+bone_name+"'", "'"+model_name+"'", xpos, ypos, zpos, zrot, scale])+"),")

                                #print("---")