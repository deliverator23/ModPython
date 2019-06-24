import random
import math

points = [

('FX_FIRE','WON_Dummy','WON_Dummy',0.065095,0.117835,6.000000,0.000000,1.000000),
('FX_SMOKE','WON_Dummy','WON_Dummy',-9.307350,-13.077141,6.000000,0.000000,1.000000),
('FX_FIRE2','WON_Dummy','WON_Dummy',13.886948,6.637851,3.000000,0.000000,1.000000)
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
							<z>%f</z>
						</m_position>
						<m_orientation>
							<x>0.000000</x>
							<y>0.000000</y>
							<z>%f</z>
						</m_orientation>
						<m_Name text="%s"/>
						<m_BoneName text="WON_Bone"/>
						<m_ModelInstanceName text="WON_Dummy"/>
						<m_scale>%f</m_scale>
					</Element>"""

tilebaseNames = ["VIL_Tribal_Thatch_Torch_A"]

angles = [-0.523599]

pos_scale_adjustment = 1

filename = "D:\\Civ6Mod\\attachment-points.xml"
with open(filename, 'w') as f:
    for i, point in enumerate(points):
        for j, angle in enumerate(angles):
            tilebaseName = random.choice(tilebaseNames)
            index = i + 1 + ((j+1) * 100)

            #attachPointName = ("Foliage" + "{:03d}".format(index))
            attachPointName = point[0]

            x = point[3] * pos_scale_adjustment
            y = point[4] * pos_scale_adjustment
            z = point[5]

            x2 = (x * math.cos(angle)) - (y * math.sin(angle))
            y2 = (y * math.cos(angle)) + (x * math.sin(angle))
            #rotation = random.random() * math.pi
            rotation = point[6]
            scale = point[7]

            print((attachmentTemplate % (tilebaseName, x2, y2, z, rotation, attachPointName, scale)),file=f)