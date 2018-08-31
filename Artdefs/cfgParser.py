import xml.etree.ElementTree as ET

xml = ET.parse("D:\\SteamLibrary\\steamapps\\common\\Sid Meier's Civilization VI SDK Assets\\pantry\\Civ6.cfg")

root = xml.getroot()

#keysStringList = []
valuesStringList = []
keyString = ""

for child in root:
    if child.tag == "m_Classes":
        for child2 in child:
            if child2.tag == "m_Classes":
                for child3 in child2:
                    if child3.attrib["class"] == "AssetObjects..TextureClass":

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
                            if child4.tag == "m_CookParams":
                                cookTuple = "new List<CookParam>(new CookParam[]{"
                                for child5 in child4: #m_Parameters
                                    for child6 in child5: #Elements
                                        for child7 in child6:
                                            if child7.tag == "m_Name":
                                                cookTuple = cookTuple + child7.attrib["text"] + "\"),"
                                            if child7.tag == "m_Default":
                                                for child8 in child7:
                                                    if ("Value") in child8.tag :
                                                        cookTuple = cookTuple + "new CookParam(\"" + child8.text + "\",\""
                                cookTuple = cookTuple + "}"
                                cookTuple = cookTuple.replace("),}",")}")
                                keys.append("CookParams")
                                values.append(cookTuple)
                            if child4.tag == "m_Name":
                                keys.insert(0, child4.tag)
                                values.insert(0, child4.attrib["text"])
 #                                   print ()  # append to list of field names
  #                                  print ()  # append to list of values
                        #keysString = "|".join(k for k in keys)
                        #valuesString = "|".join(v for v in values)
                        valuesStringList.append(values)

for values in valuesStringList:
    print("{", end='')
    print("\"{0}\"".format(values[0]), end='')
    print(", new TextureClass(", end='')

    for i, element in enumerate(values[1:]):
        if "F" in element or "D" in element or "^" in element:
            print("\"{0}\"".format(element), end='')
        elif "." in element and not "Cook" in element:
            print(element+"f", end='')
        else:
            print(element, end='')
        if i < len(values[1:]) -1:
            print(",", end='')
    print("))},", end='')
    print()


