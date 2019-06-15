import random
import math

points = [
    (34.8641,-3.02407),
(33.0454,-11.7725),
(28.7094,-19.8255),
(14.5992,-31.8841),
(9.95208,-42.4636),
(4.06176,-43.524),
(-3.88019,-35.8652),
(-21.046,-28.5185),
(-28.0415,-22.7192),
(-32.7694,-15.1647),
(34.1437,7.55272),
(31.4457,16.0465),
(26.1145,23.4049),
(2.14298,36.7703),
(-16.3797,32.9958),
(-30.6236,21.0954),
(-35.0492,13.0913),
(-36.9655,4.36373)
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

angles = [0]

xy_scale = 0.5

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