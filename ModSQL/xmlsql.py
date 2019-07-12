import xml.etree.ElementTree as ET

xml = ET.parse("D:\\mod\\GS_Reference\\Expansion_2\\Data\\Expansion2_Buildings_Major.xml")

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


#xml = ET.parse("E:\\mod\\MOAR_Units\\MoarUnits\\MOAR_Units\\Data\\MOAR_Units_Data.xml")
#xml = ET.parse("E:\\mod\\MOAR_Units\\EvenMoarUnitsAustralia\\Even_MOAR_Units_Australia\\Data\\Even_MOAR_Units_Australia_Data.xml")
#xml = ET.parse("E:\\mod\\MOAR_Units\\EvenMoarUnitsAztec\\Even_MOAR_Units_Aztec\\Data\\Even_MOAR_Units_Aztec_Data.xml")
#xml = ET.parse("E:\\mod\\MOAR_Units\\EvenMoarUnitsPoland\\Even_MOAR_Units_Poland\\Data\\Even_MOAR_Units_Poland_Data.xml")
#xml = ET.parse("E:\\mod\\MOAR_Units\\EvenMoarUnitsMacedonAndPersia_Release\\MoarUnitsMacedonAndPersia\\Data\\Even_MOAR_Units_MacedonPersia_Data.xml")
#xml = ET.parse("E:\\SteamLibrary\\steamapps\\common\\Sid Meier's Civilization VI\\Base\\Assets\\Gameplay\\Data\\Units.xml")

#xml = ET.parse("E:\\SteamLibrary\\steamapps\\common\\Sid Meier's Civilization VI\\DLC\\Expansion1\\Data\\Expansion1_Units.xml")



