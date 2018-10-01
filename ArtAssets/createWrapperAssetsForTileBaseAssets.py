import os

modbuddyPath = "D:\\Civ6Mod\\gitproject\\CivBETerrainModels\\CivBETerrainModels\\"

template = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects:AssetInstance>
	<m_BehaviorData>
		<m_behaviorDataSets>
			<m_animationBindings>
				<m_Bindings>
				</m_Bindings>
			</m_animationBindings>
			<m_timelineBindings>
				<m_Bindings>
				</m_Bindings>
			</m_timelineBindings>
			<m_timelines>
				<m_Timelines>
				</m_Timelines>
			</m_timelines>
			<m_attachmentPoints>
				<m_Points>
					<Element>
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
							<x>0.000000</x>
							<y>0.000000</y>
							<z>0.000000</z>
						</m_position>
						<m_orientation>
							<x>0.000000</x>
							<y>0.000000</y>
							<z>0.000000</z>
						</m_orientation>
						<m_Name text="AssetConnect"/>
						<m_BoneName text="NWON_Origin_Dummy"/>
						<m_ModelInstanceName text="NWON_Origin_Dummy"/>
						<m_scale>%d</m_scale>
					</Element>
				</m_Points>
			</m_attachmentPoints>
		</m_behaviorDataSets>
		<m_behaviorInstances/>
		<m_dsgName text="%s"/>
		<m_referenceGeometryNames/>
	</m_BehaviorData>
	<m_GeometrySet>
		<m_ModelInstances>
			<Element>
				<m_Name text="NWON_Origin_Dummy"/>
				<m_GeoName text="NWON_Origin_Dummy"/>
				<m_GroupStates>
					<Element>
						<m_Values>
							<m_Values>
								<Element class="AssetObjects..ObjectValue">
									<m_ObjectName text=""/>
									<m_eObjectType>MATERIAL</m_eObjectType>
									<m_ParamName text="Material"/>
								</Element>
								<Element class="AssetObjects..BoolValue">
									<m_bValue>true</m_bValue>
									<m_ParamName text="Visible"/>
								</Element>
								<Element class="AssetObjects..ObjectValue">
									<m_ObjectName text="FOW/DefaultMaterial"/>
									<m_eObjectType>MATERIAL</m_eObjectType>
									<m_ParamName text="FOWMaterial"/>
								</Element>
								<Element class="AssetObjects..ObjectValue">
									<m_ObjectName text=""/>
									<m_eObjectType>MATERIAL</m_eObjectType>
									<m_ParamName text="BurnMaterial"/>
								</Element>
								<Element class="AssetObjects..ObjectValue">
									<m_ObjectName text="DefaultSnowMaterial"/>
									<m_eObjectType>MATERIAL</m_eObjectType>
									<m_ParamName text="SnowMaterial"/>
								</Element>
							</m_Values>
						</m_Values>
						<m_GroupName text="Standardmaterial"/>
						<m_MeshName text="NWON_Origin_Dummy"/>
						<m_StateName text="Default"/>
					</Element>
				</m_GroupStates>
			</Element>
		</m_ModelInstances>
	</m_GeometrySet>
	<m_CookParams>
		<m_Values>
			<Element class="AssetObjects..BoolValue">
				<m_bValue>true</m_bValue>
				<m_ParamName text="CastShadows"/>
			</Element>
			<Element class="AssetObjects..BoolValue">
				<m_bValue>true</m_bValue>
				<m_ParamName text="CastAO"/>
			</Element>
		</m_Values>
	</m_CookParams>
	<m_Version>
		<major>0</major>
		<minor>0</minor>
		<build>0</build>
		<revision>0</revision>
	</m_Version>
	<m_ParticleEffects/>
	<m_Geometries/>
	<m_Animations/>
	<m_Materials/>
	<m_ClassName text="%s"/>
	<m_DataFiles/>
	<m_Name text="%s"/>
	<m_Description text=""/>
	<m_Tags>
		<Element text="%s"/>
	</m_Tags>
	<m_Groups/>
</AssetObjects:AssetInstance>
"""

assetClass = "TerrainElementAsset"
dsg = "Standard_TerrainElementAsset"
defaultScale = 5

assets_path = modbuddyPath + "\\Assets"

tilebaseNames = []
assetNames = []

for path, subdirs, files in os.walk(assets_path):
    for filename in files:
        if filename.endswith(".ast") and not assetClass in filename:
            unitAssetName = filename.replace(".ast","")
            tilebaseNames.append(unitAssetName)
            #print(unitAssetName)
            wrapperAssetName = unitAssetName + "_" + assetClass
            filename = assets_path + "\\" + wrapperAssetName + ".ast"
            with open(filename, 'w') as f:
                print((template % (unitAssetName,defaultScale,dsg,assetClass,wrapperAssetName,assetClass)), file=f)
            assetNames.append(wrapperAssetName)



### TerrainAssetSet_Base.xlp
xlpHeader = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects:XLP>
	<m_Version>
		<major>4</major>
		<minor>0</minor>
		<build>253</build>
		<revision>867</revision>
	</m_Version>
	<m_ClassName text="%s"/>
	<m_PackageName text="%s"/>
	<m_Entries>"""

xlpFooter = """</m_Entries>
	<m_AllowedPlatforms>
		<Element>WINDOWS</Element>
		<Element>LINUX</Element>
		<Element>MACOS</Element>
		<Element>IOS</Element>
	</m_AllowedPlatforms>
</AssetObjects:XLP>"""

xlpEntry = """<Element>
			<m_EntryID text="%s"/>
			<m_ObjectName text="%s"/>
		</Element>"""

filename = modbuddyPath + "\\XLPs\\TerrainAssetSet_Base.xlp"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(xlpHeader % ("TerrainAsset","terrain/TerrainAssetSet_Base"),file=f)
    for assetName in assetNames:
        print((xlpEntry % (assetName,assetName)),file=f)
    print(xlpFooter,file=f)

filename = modbuddyPath + "\\XLPs\\tilebases.xlp"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(xlpHeader % ("TileBase","landmarks/tilebases"),file=f)
    for assetName in tilebaseNames:
        print((xlpEntry % (assetName,assetName)),file=f)
    print(xlpFooter,file=f)


dataXMLHeader = """<?xml version="1.0" encoding="utf-8"?>
<GameInfo>
	<Types>"""

dataTypesTemplate = """<Row Type="%s" Kind="KIND_FEATURE"/>"""

dataXMLMid1 = """</Types>
	<Features>"""

dataFeaturesTemplate = """<Row FeatureType="%s" Name="Rock of Gibraltar" Tiles="1" FollowRulesInWB="false"/>"""

dataXMLMid2 = """</Features>
	<Feature_ValidTerrains>"""

dataValidTerrainsTemplate = """<Row FeatureType="%s" TerrainType="%s"/>"""

dataXMLFooter = """</Feature_ValidTerrains>
</GameInfo>"""

validTerrains = [
"TERRAIN_COAST",
"TERRAIN_OCEAN",
"TERRAIN_DESERT",
"TERRAIN_GRASS",
"TERRAIN_PLAINS",
"TERRAIN_TUNDRA",
"TERRAIN_DESERT_HILLS",
"TERRAIN_GRASS_HILLS",
"TERRAIN_PLAINS_HILLS",
"TERRAIN_TUNDRA_HILLS"
]

# Features.xml
filename = modbuddyPath + "\\Data\\Features.xml"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    #print(featuresArtdefHeader,file=f)
    print(dataXMLHeader, file=f)
    for assetName in assetNames:
        featureXMLName = "FEATURE_CIVBE_" + assetName.replace(assetClass, "").rstrip('_').upper()
        print((dataTypesTemplate % featureXMLName), file=f)

    print(dataXMLMid1, file=f)
    for assetName in assetNames:
        featureXMLName = "FEATURE_CIVBE_" + assetName.replace(assetClass, "").rstrip('_').upper()
        print((dataFeaturesTemplate % featureXMLName), file=f)

    print(dataXMLMid2, file=f)
    for assetName in assetNames:
        featureXMLName = "FEATURE_CIVBE_" + assetName.replace(assetClass, "").rstrip('_').upper()
        for terrain in validTerrains:
            print((dataValidTerrainsTemplate % (featureXMLName,terrain)), file=f)

    print(dataXMLFooter, file=f)

# Features.artdef
featuresArtdefHeader = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects:ArtDefSet>
	<m_Version>
		<major>4</major>
		<minor>0</minor>
		<build>255</build>
		<revision>871</revision>
	</m_Version>
	<m_TemplateName text="Features"/>
	<m_RootCollections>
		<Element>
			<m_CollectionName text="Feature"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>"""

featuresTemplate="""<Element>
				<m_Fields>
					<m_Values/>
				</m_Fields>
				<m_ChildCollections>
					<Element>
						<m_CollectionName text="Audio"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
					<Element>
						<m_CollectionName text="StrategicView"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
						<Element>
							<m_Fields>
								<m_Values>
									<Element class="AssetObjects..ArtDefReferenceValue">
										<m_ElementName text="Ice"/>
										<m_RootCollectionName text="Features"/>
										<m_ArtDefPath text="StrategicView.artdef"/>
										<m_CollectionIsLocked>true</m_CollectionIsLocked>
										<m_TemplateName text="StrategicView"/>
										<m_ParamName text="XrefName"/>
									</Element>
									<Element class="AssetObjects..StringValue">
										<m_Value text="1Dot"/>
										<m_ParamName text="Shape"/>
									</Element>
								</m_Values>
							</m_Fields>
							<m_ChildCollections/>
							<m_Name text="StrategicView001"/>
							<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
						</Element>
					</Element>
					<Element>
						<m_CollectionName text="Clutter"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
					<Element>
						<m_CollectionName text="Landmark"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
					<Element>
						<m_CollectionName text="Lighting"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
					<Element>
						<m_CollectionName text="ClutterVariants"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
					<Element>
						<m_CollectionName text="WaterType"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
					<Element>
						<m_CollectionName text="RevealAnimation"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
				</m_ChildCollections>
				<m_Name text="%s"/>
				<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
			</Element>"""

featuresArtdefFooter="""</Element>
	</m_RootCollections>
</AssetObjects:ArtDefSet>"""

filename = modbuddyPath + "\\ArtDefs\\Features.artdef"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(featuresArtdefHeader,file=f)
    for assetName in assetNames:
        featureXMLName = "FEATURE_CIVBE_" + assetName.replace(assetClass,"").rstrip('_').upper()
        print((featuresTemplate % (featureXMLName)),file=f)
    print(featuresArtdefFooter,file=f)


# TerrainStyle.artdef
terrainStyleArtdefHeader = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects:ArtDefSet>
	<m_Version>
		<major>4</major>
		<minor>0</minor>
		<build>250</build>
		<revision>203</revision>
	</m_Version>
	<m_TemplateName text="TerrainMaterialSet"/>
	<m_RootCollections>
		<Element>
			<m_CollectionName text="NaturalWonders"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>"""

terrainStyleArtdefFooter ="""</Element>
	</m_RootCollections>
</AssetObjects:ArtDefSet>"""

terrainStyleArtdefTemplate="""<Element>
				<m_Fields>
					<m_Values>
						<Element class="AssetObjects:BLPEntryValue">
							<m_EntryName text=""/>
							<m_XLPClass text="TerrainElement"/>
							<m_XLPPath text="TerrainElementSet_Base.xlp"/>
							<m_BLPPackage text="terrain/TerrainElementSet_Base"/>
							<m_LibraryName text="TerrainElement"/>
							<m_ParamName text="TerrainElement"/>
						</Element>
						<Element class="AssetObjects:BLPEntryValue">
							<m_EntryName text="%s"/>
							<m_XLPClass text="TerrainAsset"/>
							<m_XLPPath text="TerrainAssetSet_Base.xlp"/>
							<m_BLPPackage text="terrain/TerrainAssetSet_Base"/>
							<m_LibraryName text="TerrainAsset"/>
							<m_ParamName text="TerrainAsset"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>false</m_bValue>
							<m_ParamName text="BlockingHex1"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>false</m_bValue>
							<m_ParamName text="BlockingHex2"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>false</m_bValue>
							<m_ParamName text="BlockingHex3"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>false</m_bValue>
							<m_ParamName text="BlockingHex4"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>false</m_bValue>
							<m_ParamName text="BlockingHex5"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>false</m_bValue>
							<m_ParamName text="BlockingHex6"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>true</m_bValue>
							<m_ParamName text="DisableRotations"/>
						</Element>
						<Element class="AssetObjects:StringValue">
							<m_Value text="None"/>
							<m_ParamName text="ForceTerrainType"/>
						</Element>
						<Element class="AssetObjects:BLPEntryValue">
							<m_EntryName text=""/>
							<m_XLPClass text="Water"/>
							<m_XLPPath text=""/>
							<m_BLPPackage text=""/>
							<m_LibraryName text="Water"/>
							<m_ParamName text="WaterType"/>
						</Element>
						<Element class="AssetObjects:StringValue">
							<m_Value text="Any"/>
							<m_ParamName text="TerrainType1"/>
						</Element>
						<Element class="AssetObjects:StringValue">
							<m_Value text="Any"/>
							<m_ParamName text="TerrainType2"/>
						</Element>
						<Element class="AssetObjects:StringValue">
							<m_Value text="Any"/>
							<m_ParamName text="TerrainType3"/>
						</Element>
						<Element class="AssetObjects:StringValue">
							<m_Value text="Any"/>
							<m_ParamName text="TerrainType4"/>
						</Element>
						<Element class="AssetObjects:StringValue">
							<m_Value text="Any"/>
							<m_ParamName text="TerrainType5"/>
						</Element>
						<Element class="AssetObjects:StringValue">
							<m_Value text="Any"/>
							<m_ParamName text="TerrainType6"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>false</m_bValue>
							<m_ParamName text="RemoveCliffs"/>
						</Element>
						<Element class="AssetObjects:BoolValue">
							<m_bValue>true</m_bValue>
							<m_ParamName text="ModelHeightFromLocalHex"/>
						</Element>
					</m_Values>
				</m_Fields>
				<m_ChildCollections/>
				<m_Name text="%s"/>
				<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
			</Element>"""

filename = modbuddyPath + "\\ArtDefs\\TerrainStyle.artdef"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(terrainStyleArtdefHeader,file=f)
    for assetName in assetNames:
        featureXMLName = "FEATURE__CIVBE_" + assetName.replace(assetClass,"").rstrip('_').upper()
        print((terrainStyleArtdefTemplate % (assetName,featureXMLName)),file=f)
    print(terrainStyleArtdefFooter,file=f)