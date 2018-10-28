import os
import random

typesXMLTemplate = "INSERT INTO Types (Type, Kind) VALUES ('%s', 'KIND_UNIT');"

unitXMLTemplates = {
"INFANTRY": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PrereqTech) VALUES ('%s', '430', '6', '2', '2', 1, 'DOMAIN_LAND', '70', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_MELEE', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'TECH_REPLACEABLE_PARTS');",
"CARRIER": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech, AirSlots) VALUES ('%s', '540', '7', '3', '2', 1, 'DOMAIN_SEA', '65', 'RESOURCE_OIL', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_CARRIER', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_COMBINED_ARMS', '2');",
"SUBMARINE": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech, WMDCapable) VALUES ('%s', '680', '8', '4', '2', 0, 'DOMAIN_SEA', '80', '85', '2', 'RESOURCE_URANIUM', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_RAIDER', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_TELECOMMUNICATIONS', 1);",
"SIEGE": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, Bombard, Range, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PrereqTech) VALUES ('%s', '680', '8', '2', '3', 0, 'DOMAIN_LAND', '70', '95', '3', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_SIEGE', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'TECH_GUIDANCE_SYSTEMS');",
"AIR":"INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, CanCapture, PurchaseYield, PseudoYieldType, IgnoreMoves, PrereqTech, Stackable, PrereqDistrict, CanTargetAir) VALUES ('%s', '650', '8', '5', '5', 0, 'DOMAIN_AIR', '90', '85', '5', 'RESOURCE_ALUMINUM', 'FORMATION_CLASS_AIR', 'PROMOTION_CLASS_AIR_FIGHTER', 'ADVISOR_CONQUEST',  '%s', '%s', 0, 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_AIR_COMBAT', 1, 'TECH_LASERS', 1, 'DISTRICT_AERODROME', 1);",
"NAVAL_R": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, AntiAirCombat, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech, CanTargetAir) VALUES ('%s', '680', '8', '4', '3', 1, 'DOMAIN_SEA', '70', '85', '3', '90', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_RANGED', 'ADVISOR_CONQUEST',  '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_LASERS', 1);",
"NAVAL_M": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PseudoYieldType, PrereqTech) VALUES ('%s', '380', '5', '5', '3', 1, 'DOMAIN_SEA', '60', 'RESOURCE_COAL', 'FORMATION_CLASS_NAVAL', 'PROMOTION_CLASS_NAVAL_MELEE', 'ADVISOR_CONQUEST', '%s', '%s', 'YIELD_GOLD', 'PSEUDOYIELD_UNIT_NAVAL_COMBAT', 'TECH_STEAM_POWER');",
"RANGED": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, RangedCombat, Range, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, MandatoryObsoleteTech, PrereqTech) VALUES ('%s', '330', '5', '2', '2', 0, 'DOMAIN_LAND', '50', '60', '2', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_RANGED', 'ADVISOR_CONQUEST', '%s', '%s', 'YIELD_GOLD', 'TECH_TELECOMMUNICATIONS', 'TECH_BALLISTICS');",
"ARMOR": "INSERT INTO Units (UnitType, Cost, Maintenance, BaseMoves, BaseSightRange, ZoneOfControl, Domain, Combat, StrategicResource, FormationClass, PromotionClass, AdvisorType, Name, Description, PurchaseYield, PrereqTech) VALUES ('%s', '680', '8', '4', '2', 1, 'DOMAIN_LAND', '90', 'RESOURCE_URANIUM', 'FORMATION_CLASS_LAND_COMBAT', 'PROMOTION_CLASS_HEAVY_CAVALRY', 'ADVISOR_CONQUEST', '%s', '%s', 'YIELD_GOLD', 'TECH_COMPOSITES');",
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
																<m_fValue>1.0</m_fValue>
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
										<m_fValue>%s</m_fValue>
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
                                                                <m_ElementName text="%s"/>
                                                                <m_RootCollectionName text="UnitTintTypes"/>
                                                                <m_ArtDefPath text="Units.artdef"/>
                                                                <m_CollectionIsLocked>true</m_CollectionIsLocked>
                                                                <m_TemplateName text="Units"/>
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

with open('D:\\Civ6Mod\\Civ5Unpacks\\UnitConversionsPart2\\civ5units2.dat','r') as f:
    for x in f:
        bits = x.split(';')
        keyName = bits[0].replace(".gr2","")
        if len(bits[3].rstrip()) > 0:
            keyName = bits[3].rstrip()
        keyName = keyName.title()
        modelConvDatLines[keyName] = x



#Read Asset Names
unitAssetNames = []

# [scale, xmlType, numModels]
unitAssetTypeSettings =	{
    "Carrier": [1.5, "CARRIER", 1],
    "Naval": [1.5, "NAVAL_M", 1],
    "Infantry": [1.5, "INFANTRY", 4],
    "Ranged": [1.5, "RANGED", 2],
    "Siege": [1.5, "SIEGE", 1],
    "Sub": [1.5, "SUBMARINE", 1],
    "Cavalry": [1.5, "ARMOR", 1],
    "Air": [1.5, "AIR", 1],
    "Other": [1.5, "INFANTRY", 1]
}

unitAssetTypeOverrides = {
    "Antiaircraftgun" : "Ranged",
    "Antitankgun": "Ranged",
    "Archer" : "Ranged",
    "Artillery" : "Siege",
    "Atomicbomb" : "Air",
    "Barbarian_Archer" : "Ranged",
    "Barbarian_Euro" : "Infantry",
    "Barbarian_Galley" : "Naval",
    "Barbarian_Spearman" : "Infantry",
    "Barbarian_Swordsman": "Infantry",
    "Battleship" : "Naval",
    "Bazooka_Infantry" : "Ranged",
    "Bomber" : "Air",
    "Cannon" : "Siege",
    "Caravan" : "Cavalry",
    "Caravel" : "Naval",
    "Cargo_Ship" : "Naval",
    "Carrier" : "Carrier",
    "Catapult" : "Siege",
    "Cavalry" : "Cavalry",
    "Chariotarcher" : "Ranged",
    "Civil_War_Engineer" : "Infantry",
    "Composite_Bowman" : "Ranged",
    "Confederate_Artillery" : "Siege",
    "Confederate_Cavalry" : "Cavalry",
    "Confederate_Ironclad" : "Naval",
    "Confederate_Rifleman" : "Infantry",
    "Crossbowman" : "Ranged",
    "Cw_Great_General" : "Infantry",
    "Destroyer" : "Naval",
    "Ethiopian_Mehal_Sefari" : "Infantry",
    "Euro" : "Infantry",
    "Fighter" : "Air",
    "Frigate" : "Naval",
    "Gadrauhts_Swordsman" : "Infantry",
    "Gall" : "Naval",
    "Gatling_Gun" : "Ranged",
    "Great_Admiral" : "Naval",
    "Guidedmissile" : "Air",
    "Hand_Axe_Barbarian" : "Ranged",
    "Helicoptergunship" : "Cavalry",
    "Horseman" : "Cavalry",
    "Ironclad" : "Naval",
    "Jetfighter" : "Air",
    "Knight" : "Cavalry",
    "Lancer" : "Cavalry",
    "Mayan_Atlalist" : "Ranged",
    "Mechanizedinfantry" : "Cavalry",
    "Missilecruiser" : "Naval",
    "Mobilesam" : "Ranged",
    "Modernarmor" : "Cavalry",
    "Nuclearmissile" : "Air",
    "Nuclearsubmarine" : "Sub",
    "Rocketartillery" : "Siege",
    "Smokey_Landship" : "Cavalry",
    "Ss_" : "Cavalry",
    "Stealthbomber" : "Air",
    "Steam_Airship" : "Cavalry",
    "Steam_Fighter" : "Air",
    "Submarine" : "Sub",
    "Tank" : "Cavalry",
    "Transport" : "Naval",
    "Trebuchet" : "Siege",
    "Trireme" : "Naval",
    "Union_Artillery" : "Siege",
    "Union_Cavalry" : "Cavalry",
    "Union_Ironclad" : "Naval",
    "U_American_B17" : "Air",
    "U_Arabian_Camelarcher" : "Ranged",
    "U_Austrian_Hussar" : "Cavalry",
    "U_Byzantium_Cataphract" : "Cavalry",
    "U_Byzantium_Dromon" : "Naval",
    "U_Carthage_Africanforest_Elephant" : "Cavalry",
    "U_Carthage_Quinquereme" : "Naval",
    "U_Chinese_Chukonu" : "Ranged",
    "U_Dutch_Sea_Beggar" : "Naval",
    "U_Egyptian_Warchariot" : "Ranged",
    "U_English_Longbowman" : "Ranged",
    "U_English_Shipoftheline" : "Naval",
    "U_German_Panzer" : "Cavalry",
    "U_Greek_Companioncavalry" : "Cavalry",
    "U_Huns_Horsearcher" : "Ranged",
    "U_Indian_Warelephant" : "Cavalry",
    "U_Japanese_Zero" : "Air",
    "U_Morocco_Berber" : "Cavalry",
    "U_Ottoman_Sipahi" : "Cavalry",
    "U_Polish_Winged_Hussar" : "Cavalry",
    "U_Portugal_Carrack" : "Naval",
    "U_Roman_Ballista" : "Siege",
    "U_Russian_Cossack" : "Cavalry",
    "U_Shosone_Comanche_Rider" : "Cavalry",
    "U_Siamese_Warelephant" : "Cavalry",
    "U_Songhai_Muslimcavalry" : "Cavalry",
    "U_Spanish_Conquistador" : "Cavalry",
    "U_Spanish_Galleon" : "Naval",
    "U_Swedish_Hakkapelitta" : "Cavalry",
    "U_Venetian_Galleass" : "Naval",
    "Workboat" : "Naval",
    "Ww1_Bomber" : "Air",
    "Ww1_Fighter" : "Air",
    "Ww1_Machinegun" : "Ranged",
    "Ww1_Tank" : "Cavalry",
    "Xp_Privateer" : "Naval",
    "U_Denmark_Longboat" : "Naval",
    "U_Korean_Turtle_Ship" : "Naval",
    "U_Polynesian_War_Canoe" : "Naval"
}

unitAssetTypes = {}
modbuddyPath = "D:\\Civ6Mod\\Civ5Unpacks\\UnitConversionsPart2\\Modbuddy"
unitPrefix = "UNIT_CIV5_"
assets_path = modbuddyPath + "\\Assets"
for path, subdirs, files in os.walk(assets_path):
    for filename in files:
        if filename.endswith(".ast"):
            unitAssetName = filename.replace(".ast","")

            unitAssetNameToLookup = unitAssetName
            modelConvData = modelConvDatLines[unitAssetNameToLookup]
            animations = modelConvData.split(';')[1]

            keyFound = False
            for key in unitAssetTypeOverrides.keys():
                if unitAssetNameToLookup.startswith(key):
                    unitAssetTypes[unitAssetName] = unitAssetTypeOverrides[key]
                    keyFound = True
                    break
            if not keyFound:
                unitAssetTypes[unitAssetName] = "Other"

            unitAssetNames.append(unitAssetName)



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
        unitPrettyAssetName = unitAssetName.replace("_"," ")
        print((unitXMLTemplate % (unitDBName,unitPrettyAssetName,unitPrettyAssetName)),file=f)

# UnitBins.artdef
filename = modbuddyPath + "\\ArtDefs\\Unit_Bins.artdef"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(unitBinsHeader,file=f)
    for unitAssetName in unitAssetNames:
        unitAssetType = unitAssetTypes[unitAssetName]
        typeSettings = unitAssetTypeSettings[unitAssetType]
        print((unitBinsTemplate % (unitAssetName,unitAssetName)),file=f)
    print(unitBinsFooter,file=f)

tintStrings = ["CV_NorthernEuropean",
"CV_EastAsian",
"CV_Mediterranean",
"CV_Mughal",
"CV_NorthAfrican",
"CV_SouthAfrican",
"CV_SouthAmerican",
"CV_Any"]

# Units.artdef
filename = modbuddyPath + "\\ArtDefs\\Units.artdef"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    print(unitsArtdefHeader,file=f)
    for unitAssetName in unitAssetNames:
        unitAssetType = unitAssetTypes[unitAssetName]
        typeSettings = unitAssetTypeSettings[unitAssetType]
        scale = typeSettings[0]
        numMembers = typeSettings[2]
        unitDBName = unitPrefix + unitAssetName.upper().replace(" ","_")
        print((unitsArtdefUnitElement % (scale,numMembers,unitAssetName,unitDBName)),file=f)
    print(unitsArtdefMiddle,file=f)
    for unitAssetName in unitAssetNames:
        tintString = random.choice(tintStrings)
        print((unitsArtdefUnitMemberElement % (tintString, unitAssetName,unitAssetName)),file=f)
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