#!/usr/bin/env python
# coding: utf-8

import os
from gimpfu import *
import sys


def make_atlas(img, layer, inputFolder, outputFolder):
    index = 0

    # Iterate the folder
    for file in os.listdir(inputFolder):

        try:
            # Build the full file paths.
            inputPath = inputFolder + "\\" + file
            outputPath = outputFolder + "\\" + file

            # Open the DDS file
            image = None
            if (file.lower().endswith(('.png'))):
                image = pdb.file_png_load(inputPath, inputPath)

            # Verify if the file is an image.
            if (image != None):

                width = image.width
                height = image.height

                nw = 0
                nh = 0

                rsize = 230
                osize = 256
                rows_cols = 8

                if width > height:
                    ratio = rsize / (width * 1.0)
                    nw = rsize
                    nh = int(height * ratio)
                else:
                    ratio = rsize / (height * 1.0)
                    nw = int(width * ratio)
                    nh = rsize

                pdb.gimp_image_resize(image, osize, osize, 0, 0)

                l = image.layers[0]
                pdb.gimp_item_transform_scale(l, 0, 0, nw, nh)

                resize_offx = int((osize - nw) / 2.0)
                resize_offy = int((osize - nh) / 2.0)

                gimp.message("%d %d" % (resize_offx, resize_offy))

                pdb.gimp_layer_resize(l, osize, osize, resize_offx, resize_offy)
                l.flush()

                col_num = index % rows_cols
                row_num = index / rows_cols

                atlas_size = osize * rows_cols

                offset_x = osize * col_num
                offset_y = osize * row_num

                gimp.message("%d %d %d %d %d %d" % (width, height, col_num, row_num, offset_x, offset_y))

                pdb.gimp_layer_resize(l, atlas_size, atlas_size, offset_x, offset_y)
                l.flush()

                index += 1

                filename = outputPath.lower().replace(".png", "_256.png")

                # pdb.file_dds_save(image, image.layers[0], filename, filename, 0, 1, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0)

                pdb.file_png_save(image, image.layers[0], filename, filename, 0, 0, 0, 0, 0, 0, 0)

        except Exception as err:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            gimp.message("Unexpected error:%s %s %d" % (exc_type, fname, exc_tb.tb_lineno))


register(
    "python_fu_atlas_maker",
    "Atlas Maker",
    "Does atlas making",
    "Deliverator",
    "Open source",
    "2018",
    "<Image>/Batch/Convert/AtlasMaker",
    "*",
    [
        (PF_DIRNAME, "inputFolder", "Input directory", ""),
        (PF_DIRNAME, "outputFolder", "Output directory", "")
    ],
    [],
    make_atlas)

main()