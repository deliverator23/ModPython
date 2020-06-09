import xml.etree.ElementTree as ET
import os

models_path = "D:\\SteamLibrary\\steamapps\\common\\Sid Meier's Civilization V\\Assets\\"

with open(models_path + "\\audio_lookup.txt", 'w') as f:

    script_map = {}
    sound_map = {}

    for path, subdirs, files in os.walk(models_path):
        for filename in files:
            if filename.endswith(".xml") and "audio" in filename.lower():
                print(path, filename)
                xml = ET.parse("%s\\%s" % (path, filename))
                root = xml.getroot()
                for child in root:

                    if child.tag == "Script2DSounds":
                        for sound in child:
                            for attrib in sound:
                                if attrib.tag == 'ScriptID':
                                    script_id = attrib.text
                                if attrib.tag == 'SoundID':
                                    sound_id = attrib.text
                            script_map[script_id] = sound_id

                    if child.tag == "SoundDatas":
                        for sound in child:
                            for attrib in sound:
                                if attrib.tag == 'Filename':
                                    filename = attrib.text
                                if attrib.tag == 'SoundID':
                                    sound_id = attrib.text
                            sound_map[sound_id] = filename

    for script_id in script_map:
        sound_id = script_map[script_id]
        filename = sound_map[sound_id]
        print("\"%s\":\"%s\"," % (script_id, filename),file=f)