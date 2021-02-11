# Prunes base game TEXTURES and ANIMATIONS from SHARED_DATA

import os

#modroot = "C:\\Users\\User\\Documents\\My Games\\Sid Meier's Civilization VI\\Mods\\Warfare Expanded - Reloaded\\"
#modroot = "D:\\Civ6Mod\\gitproject\\UnitExpansion\\"

modroot = "C:\\Users\\User\\Documents\\My Games\\Sid Meier's Civilization VI\\Mods\\City Styles\\"

winblpfolder = "Platforms\\Windows\\BLPs\\"
macblpfolder  = "Platforms\\MacOS\\BLPs\\"

winmodroot = modroot+winblpfolder
macmodroot = modroot+macblpfolder

gameroot = "D:\\SteamLibrary\\steamapps\\common\\Sid Meier's Civilization VI\\Base\\Platforms\\Windows\\BLPs\\SHARED_DATA\\"



modfilelist = []

for path, subdirs, files in os.walk(winmodroot):
    for name in files:
        shortfilename = os.path.basename(name)
        modfilelist.append(shortfilename)

print("Mod File Count:", len(modfilelist))

unneededfilelist = []
for path, subdirs, files in os.walk(gameroot):
    for name in files:
        basename = os.path.basename(name)
        if basename in modfilelist:
            unneededfilelist.append(name)
            modfilelist.remove(basename)

print("Unneeded File Count:", len(unneededfilelist))

print("\nKeep in Mod:")
for name in modfilelist:
    print("<File>" + macblpfolder + name + "</File>")
for name in modfilelist:
    print("<File>" + winblpfolder + name + "</File>")

print("\nRemove from Mod:")
counter = 0
for name in unneededfilelist:
    macfilename = macmodroot + "SHARED_DATA\\" + name
    winfilename = winmodroot + "SHARED_DATA\\" + name
    print(macfilename)
    print(winfilename)

    # Uncomment to Delete Files
    #os.remove(macfilename)
    os.remove(winfilename)



#modroot = "E:\\mod\\MOAR_Units\\MoarUniqueUnits\\MoarUniqueUnits\\"
