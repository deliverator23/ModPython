import random
import math

points = [
    (45.5374, -23.4999),
    (44.4696, -19.3258),
    (43.1279, -14.7751),
    (41.5463, -8.73787),
    (39.8946, -2.44067),
    (24.1508, 43.064),
    (22.8092, 47.6147),
    (-33.8096, 36.9806),
    (-32.7384, 32.8188),
    (-33.562, -5.84282),
    (-32.4941, -10.017),
    (-31.1525, -14.5676),
    (-29.5708, -20.6048),
    (-27.9192, -26.902),
    (-26.8513, -31.0762),
    (-25.5097, -35.6268),
    (-23.8251, -41.6365),
    (3.80401, -61.5671),
    (8.5558, -60.3298)
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
						<m_BoneName text="WON_Bone"/>
						<m_ModelInstanceName text="WON_Dummy"/>
						<m_scale>0.75</m_scale>
					</Element>"""

tilebaseNames = ["Tree_C_Lg_Dirt"]

angles = [0.290000]

xy_scale = 0.38

filename = "D:\\Civ6Mod\\output\\attachment-points.xml"
with open(filename, 'w') as f:
    for i, point in enumerate(points):
        for j, angle in enumerate(angles):
            tilebaseName = random.choice(tilebaseNames)
            index = i + 1 + ((j+1) * 100)
            attachPointName = ("Foliage" + "{:03d}".format(index))

            x = point[0] * xy_scale
            y = point[1] * xy_scale

            x2 = (x * math.cos(angle)) - (y * math.sin(angle))
            y2 = (y * math.cos(angle)) + (x * math.sin(angle))
            rotation = random.random() * math.pi

            print((attachmentTemplate % (tilebaseName, x2, y2, rotation, attachPointName)),file=f)