# Prunes base game TEXTURES and ANIMATIONS from SHARED_DATA

import os

modroot = "D:\\Civ6Mod\\gitproject\\MoarUniqueUnits\\MoarUniqueUnits\\"
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

unneededfilelist = []
for path, subdirs, files in os.walk(gameroot):
    for name in files:
        basename = os.path.basename(name)
        if basename in modfilelist:
            unneededfilelist.append(name)
            modfilelist.remove(basename)

print("\nKeep in Mod:")
for name in modfilelist:
    print("<File>" + macblpfolder + name + "</File>")
for name in modfilelist:
    print("<File>" + winblpfolder + name + "</File>")

print("\nRemove from Mod:")
for name in unneededfilelist:
    macfilename = macmodroot + "SHARED_DATA\\" + name
    winfilename = winmodroot + "SHARED_DATA\\" + name
    print(macfilename)
    print(winfilename)

    # Uncomment to Delete Files
    os.remove(macfilename)
    os.remove(winfilename)



#modroot = "E:\\mod\\MOAR_Units\\MoarUniqueUnits\\MoarUniqueUnits\\"
