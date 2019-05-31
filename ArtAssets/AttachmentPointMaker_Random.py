import random
import matplotlib.pyplot as plt
import math

def PointInsideTriangle(pt, tri):
    a = 1/(-tri[1][1]*tri[2][0]+tri[0][1]*(-tri[1][0]+tri[2][0])+
        tri[0][0]*(tri[1][1]-tri[2][1])+tri[1][0]*tri[2][1])
    s = a*(tri[2][0]*tri[0][1]-tri[0][0]*tri[2][1]+(tri[2][1]-tri[0][1])*pt[0]+
        (tri[0][0]-tri[2][0])*pt[1])
    if s<0: return False
    else: t = a*(tri[0][0]*tri[1][1]-tri[1][0]*tri[0][1]+(tri[0][1]-tri[1][1])*pt[0]+
              (tri[1][0]-tri[0][0])*pt[1])
    return ((t>0) and (1-s-t>0))

NUM_POINTS_TO_GENERATE = 1200
MIN_DISTANCE = 2.25
EXCLUSION_QUAD = [[-12, 12], [-12, -12], [12, -12], [12, 12]]
OVERALL_SCALE = 22.66

points = [(random.random() * OVERALL_SCALE * 2.0 - OVERALL_SCALE, random.random() * OVERALL_SCALE * 2.0 - OVERALL_SCALE) for _ in range(NUM_POINTS_TO_GENERATE)]

xcoords = []
ycoords = []
current_points = []
for point in points:
    x,y = point

    if math.sqrt(math.pow(x,2) + math.pow(y,2)) <= OVERALL_SCALE:

        show_point = True
        for other_point in current_points:
            ox, oy = other_point
            if math.sqrt(math.pow(x - ox,2) + math.pow(y - oy,2)) <= MIN_DISTANCE:
                show_point = False
                break

        if PointInsideTriangle(point, [EXCLUSION_QUAD[0], EXCLUSION_QUAD[1], EXCLUSION_QUAD[2]]) or PointInsideTriangle(point, [EXCLUSION_QUAD[0], EXCLUSION_QUAD[2], EXCLUSION_QUAD[3]]):
            show_point = False

        if show_point:
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

def write_attachment_points(current_points):
    filename = "D:\\mod\\attachment-points.xml"
    with open(filename, 'w') as f:
        for i, point in enumerate(current_points):
            tilebaseName = random.choice(tilebaseNames)
            attachPointName = "Foliage" + str(i + 1)
            print((attachmentTemplate % (tilebaseName, point[0], point[1], attachPointName)),file=f)

write_attachment_points(current_points)