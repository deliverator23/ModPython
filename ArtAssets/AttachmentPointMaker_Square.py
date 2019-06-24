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

def PointInsideQuad(point, quad):
    return PointInsideTriangle(point, [quad[0], quad[1], quad[2]]) or PointInsideTriangle(point, [quad[0], quad[2], quad[3]])

def PointInsideHex(point, hex):
    quad1 = [hex[0], hex[1], hex[2], hex[3]]
    quad2 = [hex[0], hex[3], hex[4], hex[5]]
    return PointInsideQuad(point, quad1) or PointInsideQuad(point, quad2)


NUM_POINTS_TO_GENERATE = 2000

MIN_DISTANCE = 3
HEX_BUFFER = 3.5

SQUARE_SIZE = 22

EXCLUSION_QUAD = [[-SQUARE_SIZE, SQUARE_SIZE],
[-SQUARE_SIZE, -SQUARE_SIZE],
[SQUARE_SIZE, -SQUARE_SIZE],
[SQUARE_SIZE, SQUARE_SIZE]]

#EXCLUSION_QUAD2 = [[-6.140054, 15.87294],
#[-12.54786, 1.750044],
#[-19.36989, 21.32259],
#[-23.09389, 13.08166]]

INCLUSION_HEX = [[0, -36.5], [-32.15513,-18.22773], [-32.15513,18.22773], [0, 36.5],  [32.15513,18.22773], [32.15513,-18.22773] ]

OVERALL_SCALE = 36.5



if HEX_BUFFER > 0:
    new_hex = []

    for coord in INCLUSION_HEX:
        hex_buffer_ratio = 1 - (HEX_BUFFER / OVERALL_SCALE)
        new_coord = (coord[0] * hex_buffer_ratio, coord[1] * hex_buffer_ratio)
        new_hex.append(new_coord)

    INCLUSION_HEX = new_hex

points = [(random.random() * OVERALL_SCALE * 2.0 - OVERALL_SCALE, random.random() * OVERALL_SCALE * 2.0 - OVERALL_SCALE) for _ in range(NUM_POINTS_TO_GENERATE)]

xcoords = []
ycoords = []
current_points = []
for point in points:
    x,y = point

    #if math.sqrt(math.pow(x,2) + math.pow(y,2)) <= OVERALL_SCALE:
    if PointInsideHex(point, INCLUSION_HEX):

        show_point = True

        # Check proximity to existing points
        for other_point in current_points:
            ox, oy = other_point
            if math.sqrt(math.pow(x - ox,2) + math.pow(y - oy,2)) <= MIN_DISTANCE:
                show_point = False
                break

        if PointInsideQuad(point, EXCLUSION_QUAD): # or PointInsideQuad(point, EXCLUSION_QUAD2):
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
							<z>%f</z>
						</m_orientation>
						<m_Name text="%s"/>
						<m_BoneName text="WON_Dummy"/>
						<m_ModelInstanceName text="WON_Dummy"/>
						<m_scale>%f</m_scale>
					</Element>"""

tilebaseNames = ["VIL_Tribal_Thatch_Torch_A"]

def write_attachment_points(current_points):
    filename = "D:\\Civ6Mod\\output\\attachment-points.xml"
    with open(filename, 'w') as f:
        for i, point in enumerate(current_points):
            tilebaseName = random.choice(tilebaseNames)
            index = i + 1
            attachPointName = ("Foliage" + "{:03d}".format(index))

            scale = (random.random() / 5) + 0.9
            rotation = random.random() * math.pi

            print((attachmentTemplate % (tilebaseName, point[0], point[1], rotation, attachPointName, scale)),file=f)

write_attachment_points(current_points)