#Author: thecrazyscotsman
#Version: 2

import os
import re
import ctypes
import shutil
import glob

#USER INPUT
from sys import version_info
py3 = version_info[0] > 2

if py3:
	env = input("Please enter your project path: ")
else:
	env = raw_input("Please enter your project path: ")

#Create list of files in folders
aDir = env + "//ArtDefs"
xDir = env + "//XLPs"
artdefs = os.listdir(aDir)
xlps = os.listdir(xDir)
aList = []
xList = []

mod_art_xml_path = ""
for f in glob.glob(env + "//*.Art.xml"):
	mod_art_xml_path = f

mod_art_filename = mod_art_xml_path.split("\\")[-1]

#print(mod_art_xml_path, mod_art_filename)

#Obtain mod name and id from existing Mod.Art file
mFile = open(mod_art_xml_path, 'r')
mText = mFile.read()
mFile.close()
mName = ''.join(re.findall('<name text="(.*?)"/>', mText)[:1])
mID = ''.join(re.findall('<id text="(.*?)"/>', mText)[:1])
del mText

#Populate list with artdef file name and template name
for a in artdefs:
	tFile = open(aDir + "//" + a, 'r')
	aText = tFile.read()
	tFile.close()
	a_names = re.findall('<m_TemplateName text="(.*?)"/>', aText)[:1]
	a_list = [a] + a_names
	aList.append(a_list)

#Populate list with xlp file name and class/package names
for f in xlps:
	tFile = open(xDir + "//" + f, 'r')
	fText = tFile.read()
	tFile.close()
	f_names = re.findall('<m_ClassName text="(.*?)"/>', fText) + re.findall('<m_PackageName text="(.*?)"/>', fText)
	f_list = [f] + f_names
	xList.append(f_list)

#print mName
#print mID
#print artdefs
#print xlps
#print aList
#print xList

try:
	#Backup old Mod.Art file
	shutil.copy(env + "\\" + mod_art_filename, env + "\\" + mod_art_filename.replace(".xml","_Backup.xml"))

	#Create new Mod.Art file
	maFile = open(env + "\\" +  mod_art_filename, 'w+')

	#Write line by line
	maFile.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
	maFile.write('<AssetObjects::GameArtSpecification>\n')
	maFile.write('	<id>\n')
	maFile.write('		<name text="' + mName + '"/>\n')
	maFile.write('		<id text="' + mID + '"/>\n')
	maFile.write('	</id>\n')

	#CONSUMERS
	maFile.write('	<artConsumers>\n')
	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Units"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Units":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Cultures":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Eras":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "UnitActivities":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="Unit"/>\n')
	maFile.write('				<Element text="VFX"/>\n')
	maFile.write('				<Element text="Light"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Clutter"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	maFile.write('				<Element text="Clutter.artdef"/>\n')
	for a in aList:
		if a[1] == "Clutter":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="Landmark"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Landmarks"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Landmarks":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "CityGenerators":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Eras":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Cultures":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Civilizations":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Resources":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="CityBuildings"/>\n')
	maFile.write('				<Element text="TileBase"/>\n')
	maFile.write('				<Element text="RouteDecalMaterial"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Farms"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Farms":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="TileBase"/>\n')
	maFile.write('				<Element text="CityBuildings"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="GameLighting"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "TimeOfDay":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="ColorKey"/>\n')
	maFile.write('				<Element text="GameLighting"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="StrategicView_Properties"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "StrategicView":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="StrategicView_Sprite"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "StrategicView":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Districts":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Buildings":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="StrategicView_Sprite"/>\n')
	maFile.write('				<Element text="StrategicView_DirectedAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="StrategicView_Route"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "StrategicView":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="StrategicView_Route"/>\n')
	maFile.write('				<Element text="StrategicView_DirectedAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="StrategicView_TerrainType"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "StrategicView":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="StrategicView_TerrainBlend"/>\n')
	maFile.write('				<Element text="StrategicView_TerrainBlendCorners"/>\n')
	maFile.write('				<Element text="StrategicView_TerrainType"/>\n')
	maFile.write('				<Element text="StrategicView_DirectedAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="StrategicView_TerrainBlendCorners"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "StrategicView":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="StrategicView_TerrainBlendCorners"/>\n')
	maFile.write('				<Element text="StrategicView_DirectedAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="StrategicView_TerrainBlend"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "StrategicView":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="StrategicView_TerrainBlend"/>\n')
	maFile.write('				<Element text="StrategicView_DirectedAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Terrain"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "TerrainMaterialSet":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "GraphicsTweaks":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="TerrainAsset"/>\n')
	maFile.write('				<Element text="TerrainElement"/>\n')
	maFile.write('				<Element text="TerrainMaterial"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="WorldViewRoutes"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "WorldViewRoutes":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Eras":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="RouteDecalMaterial"/>\n')
	maFile.write('				<Element text="RouteDoodad"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="UI"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "UserInterfaceBLPs":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="UITexture"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="FOW"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "FOWConfig":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="FOWSprite"/>\n')
	maFile.write('				<Element text="FOWTexture"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="WonderMovie"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "WonderMovie":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="WonderMovie"/>\n')
	maFile.write('				<Element text="TileBase"/>\n')
	maFile.write('				<Element text="GameLighting"/>\n')
	maFile.write('				<Element text="ColorKey"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="UILensAsset"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Overlay":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="OverlayTexture"/>\n')
	maFile.write('				<Element text="UILensAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Overlay"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Overlay":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="OverlayTexture"/>\n')
	maFile.write('				<Element text="UILensAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="VFX"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "VFX":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="VFX"/>\n')
	maFile.write('				<Element text="Light"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Water"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "WaterSettings":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="Water"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="ColorKeys"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	#for a in aList:
	#	if a[1] == "ColorKeys":
	#		maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="ColorKey"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="ScreenWashEffects"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "ScreenWashEffects":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="ColorKey"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Camera"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Camera":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Terrains"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Terrains":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Features"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Features":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Civilizations"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Civilizations":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Cultures"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Cultures":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Civilizations":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')


	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Resources"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Resources":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Improvements"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="WorldView_Translate"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Districts":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Buildings":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Eras":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Features":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Resources":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Terrains":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Civilizations":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "WorldViewRoutes":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Appeal":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Cultures":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="StrategicView_Translate"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Districts":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Buildings":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Eras":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Features":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Terrains":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Routes":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Cities":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Audio"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Civilizations":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Features":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "GoodyHuts":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Terrains":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Units":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Resources":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Eras":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Districts":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Leaders":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="LeaderLighting"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Leaders":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="LeaderLighting"/>\n')
	maFile.write('				<Element text="ColorKey"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Leaders"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Leaders":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="Leader"/>\n')
	maFile.write('				<Element text="LeaderLighting"/>\n')
	maFile.write('				<Element text="ColorKey"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="LeaderFallback"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "LeaderFallback":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="LeaderFallback"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Lenses"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Lenses":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="IndirectGrid"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Features":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "GraphicsTweaks":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Terrains":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="AOSystem"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "GraphicsTweaks":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="GenericObject"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	#for a in aList:
	#	if a[1] == "GenericObject":
	#		maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Wave"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "WaveSettings":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="Wave"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="DynamicGeometry"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "DynamicGeo":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="DynamicGeometry"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="UIPreview"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "UIPreview":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="SkyBox"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "SkyBox":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="SkyBoxTexture"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="Minimap"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Minimap":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="UnitSimulation"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "UnitOperations":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
		elif a[1] == "Improvements":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>false</loadsLibraries>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<consumerName text="RangeArrows"/>\n')
	maFile.write('			<relativeArtDefPaths>\n')
	for a in aList:
		if a[1] == "Overlay":
			maFile.write('				<Element text="' + a[0] + '"/>\n')
	maFile.write('			</relativeArtDefPaths>\n')
	maFile.write('			<libraryDependencies>\n')
	maFile.write('				<Element text="OverlayTexture"/>\n')
	maFile.write('				<Element text="UILensAsset"/>\n')
	maFile.write('			</libraryDependencies>\n')
	maFile.write('			<loadsLibraries>true</loadsLibraries>\n')
	maFile.write('		</Element>\n')
	maFile.write('	</artConsumers>\n')

	#LIBRARIES
	maFile.write('	<gameLibraries>\n')
	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="CityBuildings"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "CityBuildings":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="ColorKey"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "ColorKey":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="DynamicGeometry"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "DynamicGeometry":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="FOWSprite"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "FOWSprite":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="FOWTexture"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "FOWTexture":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="GameLighting"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "GameLighting":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="Landmark"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "Landmark":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="Leader"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "Leader":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="LeaderFallback"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "LeaderFallback":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="LeaderLighting"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "LeaderLighting":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="Light"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "Light":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="OverlayTexture"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "OverlayTexture":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="RouteDecalMaterial"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "RouteDecalMaterial":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="RouteDoodad"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "RouteDoodad":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="SkyBoxTexture"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "SkyBoxTexture":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="StrategicView_DirectedAsset"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "StrategicView_DirectedAsset":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="StrategicView_Route"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "StrategicView_Route":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="StrategicView_Sprite"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "StrategicView_Sprite":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="StrategicView_TerrainBlend"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "StrategicView_TerrainBlend":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="StrategicView_TerrainBlendCorners"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "StrategicView_TerrainBlendCorners":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="StrategicView_TerrainType"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "StrategicView_TerrainType":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="TerrainAsset"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "TerrainAsset":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="TerrainElement"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "TerrainElement":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="TerrainMaterial"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "TerrainMaterial":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="TileBase"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "TileBase":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="UILensAsset"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "UILensAsset":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="UITexture"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "UITexture":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="Unit"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "Unit":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="VFX"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "VFX":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="Water"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "Water":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="Wave"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "Wave":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')

	maFile.write('		<Element>\n')
	maFile.write('			<libraryName text="WonderMovie"/>\n')
	maFile.write('			<relativePackagePaths>\n')
	for x in xList:
		if x[1] == "WonderMovie":
			maFile.write('				<Element text="' + x[2] + '"/>\n')
	maFile.write('			</relativePackagePaths>\n')
	maFile.write('		</Element>\n')
	maFile.write('	</gameLibraries>\n')

	maFile.write('	<requiredGameArtIDs>\n')
	maFile.write('		<Element>\n')
	maFile.write('			<name text="Shared"/>\n')
	maFile.write('			<id text="725760e3-7fc0-4be7-abf1-17bc756d5436"/>\n')
	maFile.write('		</Element>\n')
	maFile.write('	</requiredGameArtIDs>\n')
	maFile.write('</AssetObjects::GameArtSpecification>\n')

	#Close and save the new file, overwriting the existing one
	maFile.close()

	ctypes.windll.user32.MessageBoxW(0, u"Completed successfully", u"ModArt_Generator", 0)
except:
	ctypes.windll.user32.MessageBoxW(0, u"ERROR: Could not complete", u"ModArt_Generator", 0)

#  Message Styles:
#  0 : OK
#  1 : OK | Cancel
#  2 : Abort | Retry | Ignore
#  3 : Yes | No | Cancel
#  4 : Yes | No
#  5 : Retry | No 
#  6 : Cancel | Try Again | Continue