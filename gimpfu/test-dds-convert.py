#!/usr/bin/env python
# coding: utf-8

import os
from gimpfu import *

def dds_convert(img, layer, inputFolder, outputFolder, removeTransparency):
    ''' Inverts the colors of the PNG and JPEG images of a folder.
    
    Parameters:
    img : image The current image (unused).
    layer : layer The layer of the image that is selected (unused).
    inputFolder : string The folder of the images that must be inverted.
    outputFolder : string The folder in which save the inverted images.
    '''
    # Iterate the folder
    for file in os.listdir(inputFolder):
        try:
            # Build the full file paths.
            inputPath = inputFolder + "\\" + file
            outputPath = outputFolder + "\\" + file
        
            # Open the DDS file
            image = None
            if(file.lower().endswith(('.dds'))):
                image = pdb.file_dds_load(inputPath, inputPath, 1, 1)
                
            # Verify if the file is an image.
            if(image != None):
                # Save the image.
                if (removeTransparency == 1):
                    pdb.plug_in_threshold_alpha(image, image.layers[0], 0)
                #pdb.file_png_save(image, image.layers[0], outputPath, outputPath, 0, 9, 0, 0, 0, 0, 0)
                pdb.file_dds_save(image, image.layers[0], outputPath, outputPath,   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
        except Exception as err:
            gimp.message("Unexpected error: " + str(err))

register(
    "python_fu_test_dds_convert",
    "DDS Convert",
    "Does dds convert",
    "Deliverator",
    "Open source",
    "2018",
    "<Image>/Batch/Convert/DDS",
    "*",
    [
        (PF_DIRNAME, "inputFolder", "Input directory", ""),
        (PF_DIRNAME, "outputFolder", "Output directory", ""),
        (PF_OPTION, "removeTransparency", "Remove Transparency:", 0, ["No","Yes"])
    ],
    [],
    dds_convert)

main()
