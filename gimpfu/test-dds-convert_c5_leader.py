#!/usr/bin/env python
# coding: utf-8

import os
from gimpfu import *
import sys
import sys
from shutil import copyfile

sys.stderr = open('D:/temp/python-fu-output.txt','a')
sys.stdout=sys.stderr # So that they both go to the same file


def replace_in_paths(in_path, out_path, to_replace, with_string):
    in_rep = in_path.replace(to_replace, with_string)
    out_rep = out_path.replace(to_replace, with_string)
    return in_rep, out_rep

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
            diff_image = None
            if(file.lower().endswith('_diff.dds') and "background" not in file.lower()):

                sref_path, outputPath_sref = replace_in_paths(inputPath, outputPath, "_diff", "_sref")
                norm_path, outputPath_norm = replace_in_paths(inputPath, outputPath, "_diff", "_norm")
                blur_path, outputPath_blur = replace_in_paths(inputPath, outputPath, "_diff", "_blur")
                opac_path, outputPath_opac = replace_in_paths(inputPath, outputPath, "_diff", "_opac")
                tang_path, outputPath_tang = replace_in_paths(inputPath, outputPath, "_diff", "_tang")

                if os.path.isfile(sref_path):
                    sref_image = pdb.file_dds_load(sref_path, sref_path, 1, 1)
                    diff_image = pdb.file_dds_load(inputPath, inputPath, 1, 1)

                    if os.path.isfile(norm_path):
                        copyfile(norm_path, outputPath_norm)

                    if os.path.isfile(blur_path):
                        copyfile(blur_path, outputPath_blur)

                    if os.path.isfile(tang_path):
                        copyfile(tang_path, outputPath_tang)

                    if os.path.isfile(opac_path):
                        copyfile(opac_path, outputPath_opac)

                else:
                    print(sref_path, "not found.")
                    diff_image = None

            # Verify if the file is an image.
            if(diff_image != None):
            
                diff_layer = diff_image.layers[0]


                #diff_layer = gimp.Layer(diff_image, diff_layer.name + " DIFF", diff_layer.width, diff_layer.height, diff_layer.type, diff_layer.opacity, diff_layer.mode)
                #sref_layer = gimp.Layer(sref_image, sref_layer.name + " SREF", sref_layer.width, sref_layer.height, sref_layer.type, sref_layer.opacity, sref_layer.mode)

                # 1. Extract Alpha from SREF

                # Get the layer position.

                sref_layer = sref_image.layers[0]

                pos = 0
                for i, s_layer in enumerate(sref_image.layers):
                    if s_layer == sref_layer:
                        pos = i

                sref_layerA = gimp.Layer(sref_image, sref_layer.name + " Alpha", sref_layer.width, sref_layer.height, sref_layer.type, sref_layer.opacity, sref_layer.mode)

                sref_image.add_layer(sref_layerA, pos)

                pdb.gimp_edit_clear(sref_layerA)
                sref_layerA.flush()

                # Separate the channels.
                # Calculate the number of tiles.
                tn = int(sref_layerA.width / 128)
                if(sref_layerA.width % 128 > 0):
                    tn += 1
                tm = int(sref_layerA.height / 128)
                if(sref_layerA.height % 128 > 0):
                    tm += 1

                # Iterate over the tiles.
                for i in range(tn):
                    for j in range(tm):

                        # Get the tiles.
                        tile = sref_layer.get_tile(False, j, i)
                        tileA = sref_layerA.get_tile(False, j, i)
                        #tileRGB = layerRGB.get_tile(False, j, i)

                        # Iterate over the pixels of each tile.
                        for x in range(tile.ewidth):
                            for y in range(tile.eheight):
                                # Get the pixel and separate his colors.
                                pixel = tile[x, y]
                                pixelA = pixel[3] + pixel[3] + pixel[3] + "\xff"
                                #pixelRGB = pixel[0] + pixel[1] + pixel[2] + "\xff"

                                # Save the value in the channel layers.
                                tileA[x, y] = pixelA
                                #tileRGB[x, y] = pixelRGB

                # Update the new layers.
                tileA.flush()

                pdb.gimp_image_scale(sref_image, diff_layer.width, diff_layer.height)

                # 2. Merge Diff and Sref
                diff_layerRGB = gimp.Layer(diff_image, diff_layer.name + " Alpha", diff_layer.width, diff_layer.height, diff_layer.type, diff_layer.opacity, diff_layer.mode)

                diff_image.add_layer(diff_layerRGB, pos)

                pdb.gimp_edit_clear(diff_layerRGB)
                diff_layerRGB.flush()

                # Separate the channels.
                # Calculate the number of tiles.
                tn = int(diff_layerRGB.width / 128)
                if(diff_layerRGB.width % 128 > 0):
                    tn += 1
                tm = int(diff_layerRGB.height / 128)
                if(diff_layerRGB.height % 128 > 0):
                    tm += 1

                # Iterate over the tiles.
                for i in range(tn):
                    for j in range(tm):

                        # Get the tiles.
                        tile = diff_layer.get_tile(False, j, i)
                        tileRGB = diff_layerRGB.get_tile(False, j, i)

                        # Iterate over the pixels of each tile.
                        for x in range(tile.ewidth):
                            for y in range(tile.eheight):
                                # Get the pixel and separate his colors.
                                pixel = tile[x, y]
                                pixelRGB = pixel[0] + pixel[1] + pixel[2] + "\xff"

                                # Save the value in the channel layers.
                                tileRGB[x, y] = pixelRGB

                # Update the new layers.
                tileRGB.flush()

                new_diff_image = pdb.gimp_image_new(diff_layer.width, diff_layer.height, RGB)

                new_diff_layer = gimp.Layer(new_diff_image, diff_layer.name + " DIFF", diff_layer.width, diff_layer.height, diff_layer.type, diff_layer.opacity, diff_layer.mode)
                new_sref_layer = gimp.Layer(new_diff_image, sref_layer.name + " SREF", sref_layer.width, sref_layer.height, sref_layer.type, sref_layer.opacity, ADDITION_MODE)

                new_diff_image.add_layer(new_sref_layer, 0)
                new_diff_image.add_layer(new_diff_layer, 1)

                pdb.gimp_edit_copy(diff_layerRGB)
                floating = pdb.gimp_edit_paste(new_diff_layer,1)
                pdb.gimp_floating_sel_anchor(floating)

                pdb.gimp_edit_copy(sref_layer)
                floating = pdb.gimp_edit_paste(new_sref_layer,1)
                pdb.gimp_floating_sel_anchor(floating)

                pdb.gimp_layer_scale(new_sref_layer, diff_layer.width, diff_layer.height, False)

                merged_layer = pdb.gimp_image_merge_visible_layers(new_diff_image, 0)
                
                pdb.file_dds_save(new_diff_image, merged_layer, outputPath.lower().replace("_diff.dds","_diff_sref_a.dds"), outputPath.lower().replace("_diff.dds","_diff_sref_a.dds"),   0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
                pdb.file_dds_save(sref_image, sref_layerA, outputPath_sref.lower().replace("_sref.dds", "_sref_m.dds"), outputPath_sref.lower().replace("_sref.dds", "_sref_m.dds"), 0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)
                pdb.file_dds_save(sref_image, sref_layerA, outputPath_sref.lower().replace("_sref.dds", "_sref_g.dds"), outputPath_sref.lower().replace("_sref.dds", "_sref_g.dds"), 0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0,0, 0)

        except Exception as err:
            #gimp.message("Unexpected error: " + str(err))
            raise

register(
    "python_fu_test_dds_convert_split",
    "DDS Leader Processing",
    "Does dds leader processing",
    "Deliverator",
    "Open source",
    "2020",
    "<Image>/Batch/Convert/Civ5Leader",
    "*",
    [
        (PF_DIRNAME, "inputFolder", "Input directory", ""),
        (PF_DIRNAME, "outputFolder", "Output directory", "")
    ],
    [],
    dds_convert_split)

main()
