import xml.etree.ElementTree as ET

gameLanguages = [
    'de_DE',
    'en_US',
    'es_ES',
    'fr_FR',
    'it_IT',
    'ja_JP',
    'ko_KR',
    'pl_PL',
    'pt_BR',
    'ru_RU',
    'zh_Hans_CN',
    'zh_Hant_HK']

keepUnits = [
    'UNIT_ROCKET_ARTILLERY',
    'UNIT_SELF_PROPELLED_ARTILLERY',
    'UNIT_MORTAR',
    'UNIT_MACHINE_GUN',
    'UNIT_TREBUCHET',
    'UNIT_GATLING_GUN',
    'UNIT_MACEMAN',
    'UNIT_MEDIEVAL_HORSEMAN',
    'UNIT_RIFLEMAN',
    'UNIT_CUIRASSIER',
    'UNIT_EXPLORER',
    'UNIT_DLV_ROCKET_ARTILLERY',
    'UNIT_DLV_SELF_PROPELLED_ARTILLERY',
    'UNIT_DLV_MORTAR',
    'UNIT_DLV_MACHINE_GUN',
    'UNIT_DLV_TREBUCHET',
    'UNIT_DLV_GATLING_GUN',
    'UNIT_DLV_MACEMAN',
    'UNIT_DLV_MEDIEVAL_HORSEMAN',
    'UNIT_DLV_RIFLEMAN',
    'UNIT_DLV_CUIRASSIER',
    'UNIT_DLV_EXPLORER',
    'PLUS_X_VS_MELEE_ANTICAV_LIGHTCAV_COMBAT_BONUS_DESC',
'PLUS_20_VS_HEAVY_CAVALRY_COMBAT_BONUS_DESC',
'PLUS_15_VS_LIGHT_CAVALRY_COMBAT_BONUS_DESC']

if __name__ == '__main__':

    for lang in gameLanguages:

        pediaXML = ET.parse("E:\\mod\\MOAR_Units\\UnitExpansion\\Text\\UnitExpansion_LocalisationText_"+lang+".xml")
        root = pediaXML.getroot()

        gamedata = ET.Element('GameData')
        locText = ET.SubElement(gamedata, 'LocalizedText')

        for row in root.iter("Replace"):
            write = False
            tagName = row.get('Tag')

            print(tagName)
            if("_UNIT_" in tagName):
                for unitName in keepUnits:
                    if(unitName in tagName):
                        write = True
            else:
                for unitName in keepUnits:
                    if(unitName == tagName):
                        write = True

            if write:
                nrow = ET.SubElement(locText, 'Replace')
                nrow.set('Tag', row.get('Tag'))
                nrow.set('Language', row.get('Language'))
                nText = ET.SubElement(nrow, 'Text')
                nText.text = list(row)[0].text

        # this element holds the phonebook entries
        container = locText

        data = []
        for elem in container:
            key = elem.get('Tag')
            data.append((key, elem))

        data.sort()

        # insert the last item from each tuple
        container[:] = [item[-1] for item in data]

        ET.ElementTree(gamedata).write("E:\\mod\\XML_Rewrite\\UnitExpansion_LocalisationText_"+lang+".xml", encoding="utf-8")
