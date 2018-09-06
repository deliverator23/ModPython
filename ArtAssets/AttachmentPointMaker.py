import random

points = [(-9.25,37.667),
(-28.5,23.25),
(-19,25.5),
(-14.083,27.917),
(-10.417,23.25),
(-6.583,32.25),
(-1.583,30.917),
(2,28.333),
(-1.083,24.083),
(-0.083,36.25),
(13,27),
(18.75,19.583),
(31.083,14),
(30.667,9.75),
(30.583,5.917),
(-29.333,17.833)]

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
						<m_scale>1</m_scale>
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


filename = "D:\\mod\\output\\attachment-points.xml"
with open(filename, 'w') as f:
    for i, point in enumerate(points):
        tilebaseName = random.choice(tilebaseNames)
        attachPointName = "Foliage" + str(i)
        print((attachmentTemplate % (tilebaseName, point[0], point[1], attachPointName)),file=f)