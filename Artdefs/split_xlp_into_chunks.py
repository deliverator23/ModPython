import xml.etree.ElementTree as ET
import os

entry_bucket_ids = {}


def get_bucket_id(entry_name):
    if entry_name in entry_bucket_ids:
        return entry_bucket_ids[entry_name]
    else:
        dict_key_size = len(entry_bucket_ids.keys())
        bucket_id = int(dict_key_size / 256)
        entry_bucket_ids[entry_name] = bucket_id
        return bucket_id

base_dir = "C:\\Users\\User\\Documents\\My Games\\Sid Meier's Civilization VI\\Mods\\Warfare Expanded - Reloaded\\ArtDefs\\"
xml = ET.parse(base_dir + "Unit_Bins.artdef")

#xml = ET.parse("D:\\Civ6Mod\\gitproject\\MoarUniqueUnits\\MoarUniqueUnits\\ArtDefs\\Unit_Bins.artdef")

root = xml.getroot()

element_count = 0

for child in root:
    if child.tag == 'm_RootCollections':
        for element in child:
                isBins = False
                for child3 in element:
                    if child3.tag == 'm_CollectionName':
                        name = child3.attrib['text']
                        if name == "UnitAttachmentBins":
                            isBins = True
                        else:
                            isBins = False

                    if isBins and child3.tag == 'Element':
                        for child4 in child3:
                            if child4.tag == 'm_Name':
                                bin_group = child4.attrib['text']
                                print(">bin_group>", bin_group)
                            if child4.tag == 'm_ChildCollections':
                                for child5 in child4:
                                    for child6 in child5:
                                        for child7 in child6:
                                            if child7.tag == 'm_Name':
                                                bin_assets = child7.attrib['text']
                                                print(">bin_assets>>", bin_assets)
                                            if child7.tag == 'm_ChildCollections':
                                                for child8 in child7:
                                                    for child9 in child8:
                                                        if child9.tag == 'Element':
                                                            for child10 in child9:
                                                                if child10.tag == 'm_Name':
                                                                    bin_culture = child10.attrib['text']
                                                                    print(">bin_culture>>>", bin_culture)
                                                                if child10.tag == 'm_ChildCollections':
                                                                    for child11 in child10:
                                                                        for child12 in child11:
                                                                            if child12.tag == 'Element':
                                                                                for child13 in child12:
                                                                                    if child13.tag == 'm_Fields':
                                                                                        values = child13[0]
                                                                                        blpEntry = values[0]
                                                                                        entryName, xlpPath, blpPackage = "","",""
                                                                                        for child14 in blpEntry:
                                                                                            if child14.tag == 'm_EntryName':
                                                                                                entryName = child14.attrib['text']
                                                                                                element_count = element_count + 1

                                                                                            bucket_id = get_bucket_id(entryName)

                                                                                            if child14.tag == 'm_XLPPath':
                                                                                                xlpPath = child14.attrib['text']
                                                                                                child14.set('text', 'we_units_' + str(bucket_id) + '.xlp')

                                                                                            if child14.tag == 'm_BLPPackage':
                                                                                                blpPackage = child14.attrib['text']
                                                                                                child14.set('text', 'units/we_units_' + str(bucket_id))

                                                                                        print(">asset_entry>>>>", entryName, xlpPath, blpPackage)

print(element_count)
print(len(entry_bucket_ids.keys()))

with open(base_dir + "\\XLPs\\Unit_Bins.artdef", 'w') as f:
    xml.write(f, encoding='unicode')

xlp_map = {}

for k, v in entry_bucket_ids.items():
    if v not in xlp_map:
        xlp_map[v] = []

    xlp_map[v].append(k)


xlpHeader = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects..XLP>
	<m_Version>
		<major>4</major>
		<minor>0</minor>
		<build>253</build>
		<revision>867</revision>
	</m_Version>
	<m_ClassName text="%s"/>
	<m_PackageName text="%s"/>
	<m_Entries>"""

xlpFooter = """</m_Entries>
	<m_AllowedPlatforms>
		<Element>WINDOWS</Element>
		<Element>MACOS</Element>
	</m_AllowedPlatforms>
</AssetObjects..XLP>"""

xlpEntry = """<Element>
			<m_EntryID text="%s"/>
			<m_ObjectName text="%s"/>
		</Element>"""


for xlp_id in xlp_map:
    xlp_name = "we_units_" + str(xlp_id)
    filename = base_dir + "\\XLPs\\" + xlp_name + ".xlp"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        print(xlpHeader % ("Unit","units/" + xlp_name),file=f)
        for assetName in xlp_map[xlp_id]:
            print((xlpEntry % (assetName,assetName)),file=f)
        print(xlpFooter,file=f)


