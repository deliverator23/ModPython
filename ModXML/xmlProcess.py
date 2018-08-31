import xml.etree.ElementTree as ET

def scrapeTag(filename, topTapName, maxPara):
    pediaXML = ET.parse(filename)
    root = pediaXML.getroot()
    for row in root.iter(topTapName):
        tagName = row.get('Tag')

        languageCode = row.get('Language')

        if languageCode == None:
            languageCode = "en_US"

        textElement = list(row)[0]

        if (tagName.startswith('LOC_PEDIA_UNITS_PAGE_')):
            unitName = tagName.split('_',4)[4].rsplit('_', 4)[0]
            paraNo = int(tagName.rsplit('_', 1)[1])

            if paraNo > maxPara:
                maxPara = paraNo

            #print (('%s %s %s') % (unitName, paraNo, textElement.text))

            if not languageCode in languages:
                languages[languageCode] = {}

            currentLanguageDict = languages[languageCode]

            if not unitName in currentLanguageDict:
                currentLanguageDict[unitName] = []

            currentLanguageDict[unitName].append(textElement)

        else:

            if not languageCode in languagesOther:
                languagesOther[languageCode] = {}

            currentLanguageOtherDict = languagesOther[languageCode]

            currentLanguageOtherDict[tagName] = textElement


    return maxPara

def parseFile(filename):
    maxPara = 0
    maxPara = scrapeTag(filename, 'Replace', maxPara)
    maxPara = scrapeTag(filename, 'Row', maxPara)

gameLanguages = [
    'de_DE',
    #'en_US',
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

pediaLanguages = [
    'pt_BR',
    'de_DE',
    'es_ES',
    'ru_RU',
    'zh_Hans_CN']

transLanguages = [
    'pt_BR',
    'de_DE',
    'es_ES',
    'fr_FR',
    'it_IT',
    'ru_RU',
    'zh_Hans_CN']

#s = "LOC_PEDIA_UNITS_PAGE_UNIT_GARDE_REPUBLICAINE_CHAPTER_HISTORY_PARA_2"

languages = {}

languagesOther = {}

if __name__ == '__main__':



    # Unit Names and Descriptions etc
    parseFile("E:\\mod\\MOAR_Units\\MoarUnits\\MOAR_Units\\Text\\en_US\\MOAR_Units_Text.xml")
    for lang in transLanguages:
        parseFile("E:\\mod\\MOAR_Units\\MoarUnits\\MOAR_Units\\Text\\"+lang+"\\MOAR_Units_Text_"+lang+".xml")

    # Pedia Text etc
    parseFile("E:\\mod\\MOAR_Units\\MoarUnits\\MOAR_Units\\Text\\en_US\\MOAR_Units_GameplayText.xml")
    for lang in pediaLanguages:
        parseFile("E:\\mod\\MOAR_Units\\MoarUnits\\MOAR_Units\\Text\\"+lang+"\\MOAR_Units_GameplayText_"+lang+".xml")


    for language in gameLanguages:

        gamedata = ET.Element('GameData')
        locText = ET.SubElement(gamedata, 'LocalizedText')


        sourceOtherPedia = {}

        if language in languagesOther:
            sourceOtherPedia = languagesOther[language]
        else:
            sourceOtherPedia = languagesOther['en_US']

        for tag in sourceOtherPedia:

            row = ET.SubElement(locText, 'Replace')
            row.set('Tag',tag)
            row.set('Language', language)
            newText = ET.SubElement(row, 'Text')
            newText.text = sourceOtherPedia[tag].text


        sourcePedia = {}

        if language in languages:
            sourcePedia = languages[language]
        else:
            sourcePedia = languages['en_US']

        for unit in sourcePedia:

            for i in range(5):
                row = ET.SubElement(locText, 'Replace')
                row.set('Tag','LOC_PEDIA_UNITS_PAGE_'+unit+'_CHAPTER_HISTORY_PARA_'+str(i+1))
                row.set('Language', language)
                newText = ET.SubElement(row, 'Text')

                textValue = ""
                if i < len(sourcePedia[unit]):
                    textValue = sourcePedia[unit][i].text

                newText.text = textValue


        ET.ElementTree(gamedata).write("E:\\mod\\XML_Rewrite\\MOAR_Units_LocalisationText_"+language+".xml", encoding="utf-8")
