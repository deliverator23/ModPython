import random

points = [
# Group 1
(-9.25,37.667),
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
(-29.333,17.833),
# Group 2
(-27.417,13.083),
(-25.083,9.75),
(-21.167,7.083),
(-17.417,8.417),
(-16.833,3.667),
(-17.167,-1.25),
(-13.75,6.583),
(-13.917,2.333),
(-13.5,-1.167),
(-11.083,4.333),
(-9.917,1),
(-7.333,3.833),
(-3.667,0.333),
(-1.667,3.25),
(0.5,-1),
(2.75,3.667),
(3.417,0.75),
(3.667,-3.083),
(7,2.333),
(10.333,0.75),
(11.583,-3.583),
(9.083,-5.167),
(17.667,-0.417),
(18.167,-2.917),
(21,1),
(21.5,-2.25),
(21.333,-5.583),
(26.083,-0.917),
(24.833,-3.417),
(28.667,-0.167),
(29.167,-3.667),
(26.417,-17.083),
(24.333,-19.917),
(23.25,-16.833),
(21.25,-22.333),
(19.333,-17.583),
(-29.583,-17.583)
]

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


filename = "D:\\Civ6Mod\\output\\attachment-points.xml"
with open(filename, 'w') as f:
    for i, point in enumerate(points):
        tilebaseName = random.choice(tilebaseNames)
        attachPointName = "Foliage" + str(i)
        print((attachmentTemplate % (tilebaseName, point[0], point[1], attachPointName)),file=f)