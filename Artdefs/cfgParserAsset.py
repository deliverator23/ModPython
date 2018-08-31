import xml.etree.ElementTree as ET

xml = ET.parse("D:\\SteamLibrary\\steamapps\\common\\Sid Meier's Civilization VI SDK Assets\\pantry\\Civ6.cfg")

root = xml.getroot()

#keysStringList = []
valuesStringList = []
keyString = ""

className = "MaterialClass"

for child in root:
    if child.tag == "m_Classes":
        for child2 in child:
            if child2.tag == "m_Classes":
                for child3 in child2:
                    if child3.attrib["class"] == "AssetObjects.." + className:

                        valuesString = ""
                        keys = []
                        values = []
                        name = ""
                        for child4 in child3:
                            if child4.tag == "m_Options":
                                for child5 in child4:
                                    keys.append(child5.tag)
                                    values.append(child5.text)
                                    #print (child5.tag) #append to list of field names
                                    #print (child5.text) #append to list of values
                            if child4.tag == "m_Name":
                                keys.insert(0, child4.tag)
                                values.insert(0, child4.attrib["text"])
 #                                   print ()  # append to list of field names
  #                                  print ()  # append to list of values
                        #keysString = "|".join(k for k in keys)
                        #valuesString = "|".join(v for v in values)
                        valuesStringList.append(values)

for values in valuesStringList:
    print("\"{0}\"".format(values[0]), end='')
    print()


