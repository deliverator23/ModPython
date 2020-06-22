import xml.etree.ElementTree as ET
import os
from collections import OrderedDict
import codecs
import re

#root_path = "D:\\Civ6Mod\\gitproject\\MoarUniqueUnits\\MoarUniqueUnits\\Text"
root_path = "D:\\Civ6Mod\\gitproject\\UnitExpansion\\Text"

loc_dict = {}

#prefix = "MoarUniqueUnits_LocalisationText_"
prefix = "UnitExpansion_LocalisationText_"
suffix = ".xml"

for path, subdirs, files in os.walk(root_path):
    for file in files:

        xml = ET.parse(path + "\\" + file)

        language = file.replace(prefix,"").replace(suffix,"")

        loc_dict[language] = {}

        root = xml.getroot()

        for child in root:
            for child2 in child:
                #if child2[0].text:
                loc_dict[language][child2.attrib["Tag"]] = child2[0].text

english_dict = loc_dict["en_US"]

fixed_dict = {}

for language in loc_dict:

    fixed_dict[language] = {}

    #lang_dict = OrderedDict(sorted(loc_dict[language].items(), key=lambda t: t[0]))

    lang_dict = loc_dict[language]
    for text_key in english_dict:

        if text_key in lang_dict:
            fixed_dict[language][text_key] = lang_dict[text_key]
        else:
            fixed_dict[language][text_key] = english_dict[text_key]



for language in fixed_dict:

    fixed_lang_dict = OrderedDict(sorted(fixed_dict[language].items(), key=lambda t: t[0]))

    print(language)
    with codecs.open(root_path + "_Fix" + "\\" + prefix + language + suffix, 'w', encoding='utf8') as f:

        print("""<GameData><LocalizedText>""", file=f)

        for text_key in fixed_lang_dict:

            output_text = fixed_lang_dict[text_key]

            if not output_text:
                output_text = ""

            output_text = output_text.replace('\n', '')
            output_text = re.sub('\s+',' ',output_text)

            print(">", text_key)
            print ('<Replace Language="' + language + '" Tag="' + text_key + '"><Text>' + output_text + '</Text></Replace>', file=f)

        print("""</LocalizedText></GameData>""", file=f)
