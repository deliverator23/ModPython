import random

points = [(random.random()* 50.0 - 25, random.random()*50.0 - 25.0) for _ in range(50)]

attachmentTemplate = """<Element>
						<m_CookParams>
							<m_Values>
								<Element class="AssetObjects..BLPEntryValue">
									<m_EntryName text="%s"/>
									<m_XLPClass text="TileBase"/>
									<m_XLPPath text="tilebases.xlp"/>
									<m_BLPPackage text="landmarks/tilebases"/>
									<m_LibraryName text="TileBase"/>
									<m_ParamName text="Asset"/>
								</Element>
								<Element class="AssetObjects..StringValue">
									<m_Value text="Pivot Height"/>
									<m_ParamName text="TerrainFollowMode"/>
								</Element>
								<Element class="AssetObjects..StringValue">
									<m_Value text="OPTIONAL"/>
									<m_ParamName text="Cull Mode"/>
								</Element>
							</m_Values>
						</m_CookParams>
						<m_position>
							<x>%f</x>
							<y>%f</y>
							<z>0</z>
						</m_position>
						<m_orientation>
							<x>0.000000</x>
							<y>0.000000</y>
							<z>0</z>
						</m_orientation>
						<m_Name text="%s"/>
						<m_BoneName text="NWON_Origin_Dummy"/>
						<m_ModelInstanceName text="NWON_Origin_Dummy"/>
						<m_scale>0.75</m_scale>
					</Element>"""

tilebaseNames = ["PantanalGrassA",
"PantanalGrassB",
"PantanalPlantA",
"PantanalPlantB",
"PantanalPlantC",
"PantanalTreeBushA",
"PantanalTreeBushB",
"PantanalTreeBushC",
"PantanalTreeBushD",
"PantanalTreeA",
"PantanalTreeB",
"PantanalTreeC",
"PantanalTreeD"]


filename = "D:\\mod\\attachment-points.xml"
with open(filename, 'w') as f:
    for i, point in enumerate(points):
        tilebaseName = random.choice(tilebaseNames)
        attachPointName = "Foliage" + str(i)
        print((attachmentTemplate % (tilebaseName, point[0], point[1], attachPointName)),file=f)