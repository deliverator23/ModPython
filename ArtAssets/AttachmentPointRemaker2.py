import random
import math

points = [
('FX_FIRE',8.000000,3.900000,0.000000,1.000000),
('FX_SMOKE',-22.000000,9.000000,0.000000,1.000000),
('FX_FIRE2',-1.973653,-2.724123,0.000000,1.500000),
('Crane1',5.242378,3.166730,-2.443461,1.000000),
('Crane2',-5.167235,3.448103,1.745329,1.000000),
('Foliage001',29.752232,13.991024,0.867584,1.000000),
('Foliage002',20.479332,2.512937,0.100000,1.000000),
('Foliage003',24.110611,5.179298,0.700000,1.000000),
('Foliage004',27.627651,9.631454,0.500000,1.000000),
('Foliage005',25.929184,20.657860,0.000000,1.000000),
('Foliage006',11.826487,17.740625,1.000000,1.000000),
('Foliage007',15.165953,18.689348,1.000000,1.000000),
('Foliage008',21.680889,20.567541,1.000000,1.000000),
('Foliage009',11.984571,28.332611,1.000000,1.000000),
('Foliage010',12.394378,21.482731,1.000000,1.000000),
('Foliage011',17.755960,19.894260,1.000000,1.000000),
('Foliage012',12.425751,24.502901,1.000000,1.000000),
('Foliage013',29.939230,-2.630993,1.000000,1.000000),
('Foliage014',26.947992,-0.639460,1.000000,1.000000),
('Foliage015',23.713121,1.771422,0.000000,1.000000),
('Foliage101',-26.992790,18.770544,1.769906,1.000000),
('Foliage201',-2.759541,-32.761700,1.774919,1.000000),
('Foliage102',-12.416014,16.479092,0.974644,1.000000),
('Foliage202',-8.063403,-18.992088,0.418513,1.000000),
('Foliage103',-16.540798,18.290672,2.469821,1.000000),
('Foliage203',-7.569907,-23.470049,1.079581,1.000000),
('Foliage104',-22.155003,19.110413,2.860064,1.000000),
('Foliage204',-5.472748,-28.741974,0.923884,1.000000),
('Foliage105',-30.854883,12.126251,2.390980,1.000000),
('Foliage205',3.421499,-31.717146,2.714690,1.000000),
('Foliage106',-21.277082,1.371621,0.518620,1.000000),
('Foliage206',9.450585,-19.112352,0.226139,1.000000),
('Foliage107',-23.768444,3.789310,1.554690,1.000000),
('Foliage207',8.602469,-22.478777,2.270008,1.000000),
('Foliage108',-28.652498,8.492290,2.391836,1.000000),
('Foliage208',6.971563,-29.059973,1.972234,1.000000),
('Foliage109',-30.529028,-3.787512,0.754194,1.000000),
('Foliage209',18.544470,-24.545252,1.979734,1.000000),
('Foliage110',-24.801781,-0.007641,0.933325,1.000000),
('Foliage210',12.407397,-21.475214,1.585251,1.000000),
('Foliage111',-26.106941,5.429855,0.885796,1.000000),
('Foliage211',8.350949,-25.324244,1.398927,1.000000),
('Foliage112',-27.433002,-1.490569,0.542227,1.000000),
('Foliage212',15.007255,-23.012470,1.337408,1.000000),
('Foliage113',-12.691242,27.243568,0.673265,1.000000),
('Foliage213',-17.248127,-24.612635,0.069493,1.000000),
('Foliage114',-12.920323,23.657312,0.867628,1.000000),
('Foliage214',-14.027789,-23.017914,2.776157,1.000000),
('Foliage115',-13.390753,19.650389,2.272796,1.000000),
('Foliage215',-10.322468,-21.421873,0.924470,1.000000)
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
						<m_BoneName text="WON_Dummy"/>
						<m_ModelInstanceName text="WON_Dummy"/>
						<m_scale>%f</m_scale>
					</Element>"""

tilebaseNames = ["Jungle_PalmC"]

xy_scale = 0.85

filename = "D:\\Civ6Mod\\output\\attachment-points.xml"
with open(filename, 'w') as f:
    for i, point in enumerate(points):
        attachPointName = point[0]
        if not "Burj" in attachPointName:
            tilebaseName = random.choice(tilebaseNames)

            x = point[1] * xy_scale
            y = point[2] * xy_scale

            rotation = point[3]
            scale = point[4]

            print((attachmentTemplate % (tilebaseName, x, y, rotation, attachPointName,scale)),file=f)