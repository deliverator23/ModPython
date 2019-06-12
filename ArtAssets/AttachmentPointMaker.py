import random
import math

points = [
(29.752232,13.991024),
(20.479332, 2.512937),
(24.110611,5.179298),
(27.627651, 9.631454),
(25.929184,20.657860),
(11.826487,17.740625),
(15.165953,18.689348),
(21.680889,20.567541),
(11.984571,28.332611),
(12.394378,21.482731),
(17.755960,19.894260),
(12.425751, 24.502901),
(29.939230,-2.630993),
(26.947992,-0.639460),
(23.713121,1.771422)
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
							<z>%f</z>
						</m_orientation>
						<m_Name text="%s"/>
						<m_BoneName text="NWON_Origin_Dummy"/>
						<m_ModelInstanceName text="NWON_Origin_Dummy"/>
						<m_scale>1</m_scale>
					</Element>"""

tilebaseNames = ["Jungle_PalmC"]

angles = [2.0944, 4.18879]

filename = "D:\\Civ6Mod\\output\\attachment-points.xml"
with open(filename, 'w') as f:
    for i, point in enumerate(points):
        for j, angle in enumerate(angles):
            tilebaseName = random.choice(tilebaseNames)
            index = i + 1 + ((j+1) * 100)
            attachPointName = ("Foliage" + "{:03d}".format(index))

            x = point[0]
            y = point[1]

            x2 = (x * math.cos(angle)) - (y * math.sin(angle))
            y2 = (y * math.cos(angle)) + (x * math.sin(angle))
            rotation = random.random() * math.pi

            print((attachmentTemplate % (tilebaseName, x2, y2, rotation, attachPointName)),file=f)