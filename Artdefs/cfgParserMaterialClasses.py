import xml.etree.ElementTree as ET

xml = ET.parse("D:\\mod\\Terrain\\Exploration\\Civ6.cfg")

root = xml.getroot()

materialTypeList = []

for child in root:
    if child.tag == "m_Classes":
        for child2 in child:
            if child2.tag == "m_Classes":
                for child3 in child2:
                    if child3.attrib["class"] == "AssetObjects..MaterialClass":

                        elementList = []
                        name = ""
                        for child4 in child3:

                            if child4.tag == "m_CookParams":

                                element = ""
                                for child5 in child4:

                                    for child6 in child5:
                                        element_type = child6.attrib["class"].replace("AssetObjects..","").replace("Parameter","").replace("Object","Texture")
                                        element_name = ""
                                        element_class = ""
                                        #object_type = ""
                                        for child7 in child6:
                                            if child7.tag == "m_Name":
                                                element_name = child7.attrib["text"]
                                            if child7.tag == "m_AllowedClasses":
                                                for child8 in child7:
                                                    element_class =  child8.attrib["text"]
                                            #if child7.tag == "m_eObjectType":
                                            #    object_type = child7.text

                                        element = (element_type, element_name, element_class)
                                        elementList.append(element)

                            if child4.tag == "m_Name":
                                name = child4.attrib["text"]

                        if name not in ['SnowMaterial']:
                            materialTypeList.append((name, elementList))



for i in materialTypeList:
    print(i[0])
    for j in i[1]:
        print("-" + str(j))