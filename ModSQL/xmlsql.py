import xml.etree.ElementTree as ET

xml = ET.parse("D:\Civ6Mod\gitproject\Civilization-VI-William-of-Orange\William\Core\William_Config.xml")

root = xml.getroot()

for child in root:

    print ("")
    print ("--"+child.tag)
    if child.tag not in ('UnitPromotionModifiers','UnitAbilityModifiers','Modifiers','ModifierArguments','RequirementSets','RequirementSetRequirements','Requirements','RequirementArguments'):
        for child2 in child:

            keysString = ", ".join(child2.attrib.keys())
            values = []
            for key in child2.attrib.keys():
                value = child2.attrib[key]
                if value == 'true':
                    value = 1
                elif value == 'false':
                    value = 0
                values.append(value)

            valuesString =  ", ".join("'{0}'".format(w) for w in values)

            print ("INSERT INTO " + child.tag + " (" + keysString + ") VALUES (" + valuesString + ");")
    else:
        for child2 in child:

            keys = []
            values = []
            for child3 in child2:
                keys.append(child3.tag)

                value = child3.text
                if value == 'true':
                    value = 1
                elif value == 'false':
                    value = 0
                values.append(value)

            keysString = ", ".join(keys)
            valuesString =  ", ".join("'{0}'".format(w) for w in values)

            print ("INSERT INTO " + child.tag + " (" + keysString + ") VALUES (" + valuesString + ");")