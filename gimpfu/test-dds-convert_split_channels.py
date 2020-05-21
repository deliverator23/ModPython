#!/usr/bin/env python
# coding: utf-8

import os
from gimpfu import *

def dds_convert_split(img, layer, inputFolder, outputFolder):
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
            if(file.lower().endswith(('sref.dds'))):
                image = pdb.file_dds_load(inputPath, inputPath, 1, 1)
                
            # Verify if the file is an image.
            if(image != None):
            
                layer = image.layers[0]
                        
                # Get the layer position.
                pos = 0
                for i in range(len(image.layers)):
                    if(image.layers[i] == layer):
                        pos = i

                # Create the new layers.
                layerR = gimp.Layer(image, layer.name + " Red", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
                layerG = gimp.Layer(image, layer.name + " Green", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
                layerB = gimp.Layer(image, layer.name + " Blue", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
                layerA = gimp.Layer(image, layer.name + " Alpha", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
                layerRGB = gimp.Layer(image, layer.name + " RGB", layer.width, layer.height, layer.type, layer.opacity, layer.mode)

                image.add_layer(layerR, pos)
                image.add_layer(layerG, pos)
                image.add_layer(layerB, pos)
                image.add_layer(layerA, pos)
                image.add_layer(layerRGB, pos)
                
                # Clear the new layers.
                pdb.gimp_edit_clear(layerR)
                layerR.flush()
                pdb.gimp_edit_clear(layerG)
                layerG.flush()
                pdb.gimp_edit_clear(layerB)
                layerB.flush()
                pdb.gimp_edit_clear(layerA)
                layerA.flush()
                pdb.gimp_edit_clear(layerRGB)
                layerRGB.flush()
                
                # Separate the channels.
                # Calculate the number of tiles.
                tn = int(layer.width / 128)
                if(layer.width % 128 > 0):
                    tn += 1
                tm = int(layer.height / 128)
                if(layer.height % 128 > 0):
                    tm += 1
                
                # Iterate over the tiles.
                for i in range(tn):
                    for j in range(tm):

                        # Get the tiles.
                        tile = layer.get_tile(False, j, i)
                        tileR = layerR.get_tile(False, j, i)
                        tileG = layerG.get_tile(False, j, i)
                        tileB = layerB.get_tile(False, j, i)
                        tileA = layerA.get_tile(False, j, i)
                        tileRGB = layerRGB.get_tile(False, j, i)
                        
                        # Iterate over the pixels of each tile.
                        for x in range(tile.ewidth):
                            for y in range(tile.eheight):
                                # Get the pixel and separate his colors.
                                pixel = tile[x,y]
                                pixelR = pixel[0] + pixel[0] +  pixel[0] + "\xff"
                                pixelG = pixel[1] + pixel[1] +  pixel[1] + "\xff"
                                pixelB = pixel[2] + pixel[2] +  pixel[2] + "\xff"
                                pixelA = pixel[3] + pixel[3] +  pixel[3] + "\xff"
                                pixelRGB = pixel[0] + pixel[1] +  pixel[2] + "\xff"
                                
                                # Save the value in the channel layers.
                                tileR[x,y] = pixelR
                                tileG[x,y] = pixelG
                                tileB[x,y] = pixelB
                                tileA[x,y] = pixelA
                                tileRGB[x,y] = pixelRGB
                
                # Update the new layers.
                tileR.flush()
                tileG.flush()
                tileB.flush()
                tileA.flush()
                tileRGB.flush()

                #pdb.file_dds_save(image, layerR, outputPath.lower().replace(".dds","_r.dds"), outputPath.lower().replace(".dds","_r.dds"),   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
                #pdb.file_dds_save(image, layerG, outputPath.lower().replace(".dds","_g.dds"), outputPath.lower().replace(".dds","_g.dds"),   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
                #pdb.file_dds_save(image, layerB, outputPath.lower().replace(".dds","_b.dds"), outputPath.lower().replace(".dds","_b.dds"),   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
                #pdb.file_dds_save(image, layerA, outputPath.lower().replace(".dds","_a.dds"), outputPath.lower().replace(".dds","_a.dds"),   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
                pdb.file_dds_save(image, layerRGB, outputPath.lower().replace(".dds","_rgb.dds"), outputPath.lower().replace(".dds","_rgb.dds"),   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
                
                #pdb.gimp_invert(layerA)
                #pdb.gimp_drawable_levels_stretch(layerA)
                #pdb.gimp_drawable_levels(layerA, 0, 0, 0.902, 0, 1, 0, 1, 0)
                
                pdb.file_dds_save(image, layerA, outputPath.lower().replace(".dds","_alpha.dds"), outputPath.lower().replace(".dds","_alpha.dds"),   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
            
        except Exception as err:
            gimp.message("Unexpected error: " + str(err))

register(
    "python_fu_test_dds_convert_split",
    "DDS Convert Split",
    "Does dds convert split",
    "Deliverator",
    "Open source",
    "2018",
    "<Image>/Batch/Convert/DDSSplit",
    "*",
    [
        (PF_DIRNAME, "inputFolder", "Input directory", ""),
        (PF_DIRNAME, "outputFolder", "Output directory", "")
    ],
    [],
    dds_convert_split)

main()
