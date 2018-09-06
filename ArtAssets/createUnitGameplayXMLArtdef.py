import os

typesXMLTemplate = "INSERT INTO Types (Type, Kind) VALUES ('%s', 'KIND_UNIT');"

unitXMLTemplates = {
"INFANTRY": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PrereqTech) VALUES ('%s', '430', '6', '2', '2', 'true', 'DOMAIN_LAND', '70', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_MELEE', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'TECH_REPLACEABLE_PARTS');",
"CARRIER": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech, AirSlots) VALUES ('%s', '540', '7', '3', '2', 'true', 'DOMAIN_SEA', '65', 'RESOURCE_OIL', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_CARRIER', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_COMBINED_ARMS', '2');",
"SUBMARINE": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech, WMDCapable) VALUES ('%s', '680', '8', '4', '2', 'false', 'DOMAIN_SEA', '80', '85', '2', 'RESOURCE_URANIUM', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_RAIDER', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_TELECOMMUNICATIONS', 'true');",
"SIEGE": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, Bombard, Range, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PrereqTech) VALUES ('%s', '680', '8', '2', '3', 'false', 'DOMAIN_LAND', '70', '95', '3', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_SIEGE', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'TECH_GUIDANCE_SYSTEMS');",
"AIR":"INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, CanCapture, PurchaseYield, PseudoYieldType, IgnoreMoves, PrereqTech, Stackable, PrereqDistrict, CanTargetAir) VALUES ('%s', '650', '8', '5', '5', 'false', 'DOMAIN_AIR', '90', '85', '5', 'RESOURCE_ALUMINUM', 'FORMATION_CLASS_AIR', 'PROMOTION_CLASS_AIR_FIGHTER', 'ADVISOR_CONQUEST',  '%s', '%s', 'False', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_AIR_COMBAT', 'true', 'TECH_LASERS', 'TRUE', 'DISTRICT_AERODROME', 'TRUE');",
"NAVAL_R": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, AntiAirCombat, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech, CanTargetAir) VALUES ('%s', '680', '8', '4', '3', 'true', 'DOMAIN_SEA', '70', '85', '3', '90', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_RANGED', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_LASERS', 'TRUE');",
"NAVAL_M": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech) VALUES ('%s', '380', '5', '5', '3', 'true', 'DOMAIN_SEA', '60', 'RESOURCE_COAL', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_MELEE', 'ADVISOR_CONQUEST', '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_STEAM_POWER');",
"RANGED": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, MandatoryObsoleteTech, PrereqTech) VALUES ('%s', '330', '5', '2', '2', 'false', 'DOMAIN_LAND', '50', '60', '2', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_RANGED', 'ADVISOR_CONQUEST', '%s', '%s', 'YIELD_GOLD', 'TECH_TELECOMMUNICATIONS', 'TECH_BALLISTICS');",
"ARMOR": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PrereqTech) VALUES ('%s', '680', '8', '4', '2', 'true', 'DOMAIN_LAND', '90', 'RESOURCE_URANIUM', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_HEAVY_CAVALRY', 'ADVISOR_CONQUEST', '%s', '%s', 'YIELD_GOLD', 'TECH_COMPOSITES');",
"DEFAULT": "INSERT INTO Units (UnitType, BaseMoves, Cost, AdvisorType, BaseSightRange, ZoneOfControl, Domain, FormationClass, Name, Description, PurchaseYield, PromotionClass, Maintenance, Combat) VALUES ('%s', '50', '10', 'ADVISOR_CONQUEST', '2', 1, 'DOMAIN_LAND', 'FORMATION_CLASS_LAND_COMBAT', '%s', '%s', 'YIELD_GOLD', 'PROMOTION_CLASS_HEAVY_CAVALRY', '1', '90');"
}

unitBinsHeader = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects:ArtDefSet>
	<m_Version>
		<major>4</major>
		<minor>0</minor>
		<build>253</build>
		<revision>867</revision>
	</m_Version>
	<m_TemplateName text="Units"/>
	<m_RootCollections>
		<Element>
			<m_CollectionName text="Units"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitMovementTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitFormationTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="MemberCombat"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitCombat"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="CombatAttack"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitFormationLayoutTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="CombatFormation"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitDomainTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitAttachmentBins"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
			<Element>
				<m_Fields>
					<m_Values/>
				</m_Fields>
				<m_ChildCollections>
					<Element>
						<m_CollectionName text="Groups"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>"""

unitBinsFooter = """</Element>
				</m_ChildCollections>
				<m_Name text="Units"/>
				<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
			</Element>
		</Element>
		<Element>
			<m_CollectionName text="UnitMemberTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitTintTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitGlobals"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
	</m_RootCollections>
</AssetObjects:ArtDefSet>"""

unitBinsTemplate = """<Element>
							<m_Fields>
								<m_Values/>
							</m_Fields>
							<m_ChildCollections>
								<Element>
									<m_CollectionName text="Cultures"/>
									<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
									<Element>
										<m_Fields>
											<m_Values/>
										</m_Fields>
										<m_ChildCollections>
											<Element>
												<m_CollectionName text="Assets"/>
												<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
												<Element>
													<m_Fields>
														<m_Values>
															<Element class="AssetObjects:BLPEntryValue">
																<m_EntryName text="%s"/>
																<m_XLPClass text="Unit"/>
																<m_XLPPath text="Units.xlp"/>
																<m_BLPPackage text="units/units"/>
																<m_LibraryName text="Unit"/>
																<m_ParamName text="Asset"/>
															</Element>
															<Element class="AssetObjects:FloatValue">
																<m_fValue>%s</m_fValue>
																<m_ParamName text="Scale"/>
															</Element>
														</m_Values>
													</m_Fields>
													<m_ChildCollections/>
													<m_Name text="A"/>
													<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
												</Element>
											</Element>
										</m_ChildCollections>
										<m_Name text="Any"/>
										<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
									</Element>
								</Element>
							</m_ChildCollections>
							<m_Name text="%s"/>
							<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
						</Element>"""

unitsArtdefHeader = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects:ArtDefSet>
	<m_Version>
		<major>4</major>
		<minor>0</minor>
		<build>253</build>
		<revision>293</revision>
	</m_Version>
	<m_TemplateName text="Units"/>
	<m_RootCollections>
		<Element>
			<m_CollectionName text="Units"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>"""


unitsArtdefMiddle = """</Element>
		<Element>
			<m_CollectionName text="UnitMovementTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitFormationTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="MemberCombat"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitCombat"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="CombatAttack"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitFormationLayoutTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="CombatFormation"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitDomainTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitAttachmentBins"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitMemberTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>"""

unitsArtdefFooter = """</Element>
		<Element>
			<m_CollectionName text="UnitTintTypes"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
		<Element>
			<m_CollectionName text="UnitGlobals"/>
			<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
		</Element>
	</m_RootCollections>
</AssetObjects:ArtDefSet>"""

unitsArtdefUnitElement = """<Element>
				 <m_Fields>
                    <m_Values>
                        <Element class="AssetObjects:ArtDefReferenceValue">
                            <m_ElementName text="Horsemen"/>
                            <m_RootCollectionName text="UnitFormationTypes"/>
                            <m_ArtDefPath text="Units.artdef"/>
                            <m_CollectionIsLocked>true</m_CollectionIsLocked>
                            <m_TemplateName text="Units"/>
                            <m_ParamName text="Formation"/>
                        </Element>
                        <Element class="AssetObjects:ArtDefReferenceValue">
                            <m_ElementName text="Knight"/>
                            <m_RootCollectionName text="UnitCombat"/>
                            <m_ArtDefPath text="Units.artdef"/>
                            <m_CollectionIsLocked>true</m_CollectionIsLocked>
                            <m_TemplateName text="Units"/>
                            <m_ParamName text="UnitCombat"/>
                        </Element>
                        <Element class="AssetObjects:ArtDefReferenceValue">
                            <m_ElementName text=""/>
                            <m_RootCollectionName text="UnitFormationTypes"/>
                            <m_ArtDefPath text="Units.artdef"/>
                            <m_CollectionIsLocked>true</m_CollectionIsLocked>
                            <m_TemplateName text=""/>
                            <m_ParamName text="EscortFormation"/>
                        </Element>
                        <Element class="AssetObjects:ArtDefReferenceValue">
                            <m_ElementName text="UNIT_ANCIENTEMBARK"/>
                            <m_RootCollectionName text="Units"/>
                            <m_ArtDefPath text="Units.artdef"/>
                            <m_CollectionIsLocked>true</m_CollectionIsLocked>
                            <m_TemplateName text="Units"/>
                            <m_ParamName text="EmbarkedUnit"/>
                        </Element>
                        <Element class="AssetObjects:BoolValue">
                            <m_bValue>false</m_bValue>
                            <m_ParamName text="DoNotDisplayCharges"/>
                        </Element>
                        <Element class="AssetObjects:ArtDefReferenceValue">
                            <m_ElementName text=""/>
                            <m_RootCollectionName text="UnitCulture"/>
                            <m_ArtDefPath text="Cultures.artdef"/>
                            <m_CollectionIsLocked>true</m_CollectionIsLocked>
                            <m_TemplateName text=""/>
                            <m_ParamName text="Culture"/>
                        </Element>
                        <Element class="AssetObjects:ArtDefReferenceValue">
                            <m_ElementName text=""/>
                            <m_RootCollectionName text="Era"/>
                            <m_ArtDefPath text="Eras.artdef"/>
                            <m_CollectionIsLocked>true</m_CollectionIsLocked>
                            <m_TemplateName text=""/>
                            <m_ParamName text="Era"/>
                        </Element>
                        <Element class="AssetObjects:ArtDefReferenceValue">
                            <m_ElementName text=""/>
                            <m_RootCollectionName text="Units"/>
                            <m_ArtDefPath text="Units.artdef"/>
                            <m_CollectionIsLocked>true</m_CollectionIsLocked>
                            <m_TemplateName text=""/>
                            <m_ParamName text="ProxyUnit"/>
                        </Element>
                        <Element class="AssetObjects:BoolValue">
                            <m_bValue>false</m_bValue>
                            <m_ParamName text="PlayDeathOnDestroy"/>
                        </Element>
                        <Element class="AssetObjects:IntValue">
                            <m_nValue>0</m_nValue>
                            <m_ParamName text="DisplayLevel"/>
                        </Element>
                    </m_Values>
                </m_Fields>
				<m_ChildCollections>
					<Element>
						<m_CollectionName text="Members"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
						<Element>
							<m_Fields>
								<m_Values>
									<Element class="AssetObjects:FloatValue">
										<m_fValue>1.000000</m_fValue>
										<m_ParamName text="Scale"/>
									</Element>
									<Element class="AssetObjects:IntValue">
										<m_nValue>%s</m_nValue>
										<m_ParamName text="Count"/>
									</Element>
									<Element class="AssetObjects:ArtDefReferenceValue">
										<m_ElementName text="UnitMember_%s"/>
										<m_RootCollectionName text="UnitMemberTypes"/>
										<m_ArtDefPath text="Units.artdef"/>
										<m_CollectionIsLocked>true</m_CollectionIsLocked>
										<m_TemplateName text="Units"/>
										<m_ParamName text="Type"/>
									</Element>
								</m_Values>
							</m_Fields>
							<m_ChildCollections/>
							<m_Name text="A"/>
							<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
						</Element>
					</Element>
					<Element>
						<m_CollectionName text="Audio"/>
						<m_ReplaceMergedCollectionElements>false</m_ReplaceMergedCollectionElements>
					</Element>
				</m_ChildCollections>
				<m_Name text="%s"/>
				<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
			</Element>"""

unitsArtdefUnitMemberElement = """<Element>
				<m_Fields>
					<m_Values>
						<Element class="AssetObjects:ArtDefReferenceValue">
							<m_ElementName text="Tank"/>
							<m_RootCollectionName text="UnitMovementTypes"/>
							<m_ArtDefPath text="Units.artdef"/>
							<m_CollectionIsLocked>true</m_CollectionIsLocked>
							<m_TemplateName text=""/>
							<m_ParamName text="Movement"/>
						</Element>
						<Element class="AssetObjects:ArtDefReferenceValue">
							<m_ElementName text="TankCombat"/>
							<m_RootCollectionName text="MemberCombat"/>
							<m_ArtDefPath text="Units.artdef"/>
							<m_CollectionIsLocked>true</m_CollectionIsLocked>
							<m_TemplateName text=""/>
							<m_ParamName text="Combat"/>
						</Element>
						<Element class="AssetObjects:ArtDefReferenceValue">
							<m_ElementName text="METAL"/>
							<m_RootCollectionName text="MaterialTypes"/>
							<m_ArtDefPath text="VFX.artdef"/>
							<m_CollectionIsLocked>true</m_CollectionIsLocked>
							<m_TemplateName text=""/>
							<m_ParamName text="VFXMaterialType"/>
						</Element>
						<Element class="AssetObjects:ArtDefReferenceValue">
							<m_ElementName text="METAL"/>
							<m_RootCollectionName text="MaterialTypes"/>
							<m_ArtDefPath text="VFX.artdef"/>
							<m_CollectionIsLocked>true</m_CollectionIsLocked>
							<m_TemplateName text=""/>
							<m_ParamName text="VFXWeaponImpact"/>
						</Element>
						<Element class="AssetObjects:FloatValue">
							<m_fValue>0.000000</m_fValue>
							<m_ParamName text="ImpactHeightOverride"/>
						</Element>
					</m_Values>
				</m_Fields>
				<m_ChildCollections>
					<Element>
						<m_CollectionName text="Cultures"/>
						<Element>
							<m_Fields>
								<m_Values/>
							</m_Fields>
							<m_ChildCollections>
								<Element>
									<m_CollectionName text="Variations"/>
									<Element>
										<m_Fields>
											<m_Values>
												<Element class="AssetObjects:FloatValue">
													<m_fValue>1.0</m_fValue>
													<m_ParamName text="Scale"/>
												</Element>
												<Element class="AssetObjects:BoolValue">
													<m_bValue>false</m_bValue>
													<m_ParamName text="IsAttachment"/>
												</Element>
											</m_Values>
										</m_Fields>
										<m_ChildCollections>
											<Element>
												<m_CollectionName text="Attachments"/>
												<Element>
													<m_Fields>
														<m_Values>
															<Element class="AssetObjects:StringValue">
																<m_Value text="Root"/>
																<m_ParamName text="Point"/>
															</Element>
															<Element class="AssetObjects:ArtDefReferenceValue">
																<m_ElementName text=""/>
																<m_RootCollectionName text="UnitTintTypes"/>
																<m_ArtDefPath text=""/>
																<m_CollectionIsLocked>true</m_CollectionIsLocked>
																<m_TemplateName text=""/>
																<m_ParamName text="Tint"/>
															</Element>
														</m_Values>
													</m_Fields>
													<m_ChildCollections>
														<Element>
															<m_CollectionName text="Bins"/>
															<Element>
																<m_Fields>
																	<m_Values/>
																</m_Fields>
																<m_ChildCollections/>
																<m_Name text="Units/%s"/>
																<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
															</Element>
														</Element>
													</m_ChildCollections>
													<m_Name text="Root"/>
													<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
												</Element>
											</Element>
										</m_ChildCollections>
										<m_Name text="A"/>
										<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
									</Element>
								</Element>
							</m_ChildCollections>
							<m_Name text="Any"/>
							<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
						</Element>
					</Element>
				</m_ChildCollections>
				<m_Name text="UnitMember_%s"/>
				<m_AppendMergedParameterCollections>false</m_AppendMergedParameterCollections>
			</Element>"""



modelConvDatLines = {}

with open('D:\\mod\\BeyondEarthUnpacks\\UnitModels\\resaveBatch\\unit_models.dat','r') as f:
    for x in f:
        bits = x.split(';')
        keyName = bits[0].replace(".gr2","")
        if len(bits[3].rstrip()) > 0:
            keyName = bits[3].rstrip()
        modelConvDatLines[keyName] = x



#Read Asset Names
unitAssetNames = []
unitAssetTypes = {}
modbuddyPath = "D:\\mod\\BeyondEarthUnpacks\\UnitModels\\resaveBatch\\Modbuddy"
unitPrefix = "UNIT_CIVBE_"
assets_path = modbuddyPath + "\\Assets"
for path, subdirs, files in os.walk(assets_path):
    for filename in files:
        if filename.endswith(".ast"):
            unitAssetName = filename.replace(".ast","")
            modelConvData = modelConvDatLines[unitAssetName]
            animations = modelConvData.split(';')[1]
            if (animations.startswith("Naval_Carrier")):
                unitAssetTypes[unitAssetName] = "NavalCarrier"
            elif (animations.startswith("NavalMelee")):
                unitAssetTypes[unitAssetName] = "NavalMelee"
            elif (animations.startswith("Naval_Fighter") or animations.startswith("NavalFighter")):
                unitAssetTypes[unitAssetName] = "NavalFighter"
            elif (animations.startswith("Marine")):
                unitAssetTypes[unitAssetName] = "Marine"
            elif (animations.startswith("RangedMarine")):
                unitAssetTypes[unitAssetName] = "RangedMarine"
            elif (animations.startswith("Satellite")):
                unitAssetTypes[unitAssetName] = "Satellite"
            elif (animations.startswith("Siege")):
                unitAssetTypes[unitAssetName] = "Siege"
            elif (animations.startswith("Sub")):
                unitAssetTypes[unitAssetName] = "Sub"
            elif (animations.startswith("Cavalry")):
                unitAssetTypes[unitAssetName] = "Cavalry"
            elif (animations.startswith("Hydracoral")):
                unitAssetTypes[unitAssetName] = "Hydracoral"
            elif (animations.startswith("Air_Fighter")):
                unitAssetTypes[unitAssetName] = "AirFighter"
            else:
                unitAssetTypes[unitAssetName] = "Other"
            unitAssetNames.append(unitAssetName)

# [scale, xmlType, numModels]
unitAssetTypeSettings =	{
    "NavalCarrier": [0.3, "CARRIER", 1],
    "NavalMelee": [1, "NAVAL_M", 1],
    "NavalFighter": [1, "NAVAL_M", 1],
    "Marine": [1.5, "INFANTRY", 4],
    "RangedMarine": [1.5, "RANGED", 2],
    "Satellite": [1, "AIR", 1],
    "Siege": [1, "SIEGE", 1],
    "Sub": [1, "SUBMARINE", 1],
    "Cavalry": [1, "ARMOR", 1],
    "Hydracoral": [10, "NAVAL_M", 1],
    "AirFighter": [1, "AIR", 1],
    "Other": [1, "ARMOR", 1]
}

#UnitsData.sql
filename = modbuddyPath + "\\Data\\UnitsData.sql"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print("--Types",file=f)
    for unitAssetName in unitAssetNames:
        unitDBName = unitPrefix + unitAssetName.upper().replace(" ","_")
        print((typesXMLTemplate % unitDBName),file=f)

    print("",file=f)
    print("--Units",file=f)
    for unitAssetName in unitAssetNames:
        unitDBName = unitPrefix + unitAssetName.upper().replace(" ","_")
        unitAssetType = unitAssetTypes[unitAssetName]
        typeSettings = unitAssetTypeSettings[unitAssetType]
        unitXMLTemplate = unitXMLTemplates[typeSettings[1]]
        print((unitXMLTemplate % (unitDBName,unitAssetName,unitAssetName)),file=f)

# UnitBins.artdef
filename = modbuddyPath + "\\ArtDefs\\Unit_Bins.artdef"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(unitBinsHeader,file=f)
    for unitAssetName in unitAssetNames:
        unitAssetType = unitAssetTypes[unitAssetName]
        typeSettings = unitAssetTypeSettings[unitAssetType]
        scale = typeSettings[0]
        print((unitBinsTemplate % (unitAssetName,scale,unitAssetName)),file=f)
    print(unitBinsFooter,file=f)

# Units.artdef
filename = modbuddyPath + "\\ArtDefs\\Units.artdef"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(unitsArtdefHeader,file=f)
    for unitAssetName in unitAssetNames:
        unitAssetType = unitAssetTypes[unitAssetName]
        typeSettings = unitAssetTypeSettings[unitAssetType]
        numMembers = typeSettings[2]
        unitDBName = unitPrefix + unitAssetName.upper().replace(" ","_")
        print((unitsArtdefUnitElement % (numMembers,unitAssetName,unitDBName)),file=f)
    print(unitsArtdefMiddle,file=f)
    for unitAssetName in unitAssetNames:
        print((unitsArtdefUnitMemberElement % (unitAssetName,unitAssetName)),file=f)
    print(unitsArtdefFooter,file=f)


# Units.xlp

xlpHeader = """<?xml version="1.0" encoding="UTF-8" ?>
<AssetObjects:XLP>
	<m_Version>
		<major>4</major>
		<minor>0</minor>
		<build>253</build>
		<revision>867</revision>
	</m_Version>
	<m_ClassName text="Unit"/>
	<m_PackageName text="units/units"/>
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

filename = modbuddyPath + "\\XLPs\\units.xlp"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(xlpHeader,file=f)
    for unitAssetName in unitAssetNames:
        print((xlpEntry % (unitAssetName,unitAssetName)),file=f)
    print(xlpFooter,file=f)