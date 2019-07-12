import csv

type_template = "<Row Type=\"GREATWORK_%s\" Kind=\"KIND_GREATWORK\"/>"
greatwork_art_template = "<Row GreatWorkType=\"GREATWORK_%s\" GreatWorkObjectType=\"GREATWORKOBJECT_%s\" Name=\"LOC_GREATWORK_%s_NAME\" Tourism=\"%s\" EraType=\"%s\"/>"
yield_template = "<Row GreatWorkType=\"GREATWORK_%s\" YieldType=\"%s\" YieldChange=\"%s\"/>"
text_template = """<Row Tag="LOC_GREATWORK_%s_NAME" Language="en-US">
			<Text>%s</Text>
		</Row>"""

art_template = """<Element>
			<m_EntryID text="%s"/>
			<m_ObjectName text="%s"/>
		</Element>"""

icon_template = "<Row Name=\"ICON_GREATWORK_%s\" Atlas=\"ICON_ATLAS_UNE_GREATWORKS_%s\" Index=\"%s\"/>"

artifacts = []
relics = []

with open('D:\\Civ6Mod\\Artifacts_and_Relics\\Unearthed.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        artifacts.append((row[0], row[1], row[2]))




with open('D:\\Civ6Mod\\Artifacts_and_Relics\\Unearthed.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        if len(row[5]) > 0:
            relic_type = row[5]
            relic_name = row[6]
            relics.append((row[5], row[6]))

for artifact in artifacts:
    print(type_template % artifact[0])

print("\n")

for artifact in artifacts:
    print(greatwork_art_template % (artifact[0], "ARTIFACT", artifact[0], "3", "ERA_" + artifact[2].upper()))

print("\n")

for artifact in artifacts:
    print(yield_template % (artifact[0], "YIELD_CULTURE", 3))

print("\n")

for artifact in artifacts:
    print(text_template % (artifact[0], artifact[1]))

print("\n")

for artifact in artifacts:
    print(art_template % (artifact[0], artifact[0]))

print("\n")

for i, artifact in enumerate(artifacts):
    print(icon_template % (artifact[0], "ARTIFACTS", i))

print("\n")


for relic in relics:
    print(type_template % relic[0])

print("\n")

for relic in relics:
    print(greatwork_art_template % (relic[0], "RELIC", relic[0], "8", ""))

print("\n")

for relic in relics:
    print(yield_template % (relic[0], "YIELD_FAITH", 4))

print("\n")

for relic in relics:
    print(text_template % (relic[0], relic[1]))

print("\n")

for relic in relics:
    print(art_template % (relic[0], relic[0]))

print("\n")

for i, relic in enumerate(relics):
    print(icon_template % (relic[0], "RELICS", i))

print("\n")