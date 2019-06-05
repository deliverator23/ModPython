import random
import matplotlib.pyplot as plt
import math

points = []

RADIUS = 20
NUMBER_OF_POINTS = 20

degree_step = 360.0 / NUMBER_OF_POINTS

for degree in range(0, 360, int(degree_step)):
    angle = degree * math.pi / 180
    x = RADIUS * math.cos(angle)
    y = RADIUS * math.sin(angle)
    point = [x,y]
    points.append(point)

xcoords = []
ycoords = []
current_points = []
for point in points:
    x,y = point
    xcoords.append(x)
    ycoords.append(y)
    current_points.append(point)

print(str(len(current_points)) + " points written.")

plt.scatter(xcoords,ycoords)
plt.axes().set_aspect('equal', 'datalim')
plt.show()

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
						<m_scale>%f</m_scale>
					</Element>"""

tilebaseNames = ["Tree_B_Lg_Dirt", "Tree_C_Lg_Dirt"]

def write_attachment_points(current_points):
    filename = "D:\\mod\\attachment-points.xml"
    with open(filename, 'w') as f:
        for i, point in enumerate(current_points):
            tilebaseName = random.choice(tilebaseNames)
            index = i + 1
            attachPointName = ("Foliage" + "{:03d}".format(index))

            scale = 1.0
            rotation = random.random() * math.pi

            print((attachmentTemplate % (tilebaseName, point[0], point[1], rotation, attachPointName, scale)),file=f)

write_attachment_points(current_points)