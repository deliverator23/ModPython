#!/usr/bin/env python
#


from gimpfu import *

def split_channels(img, layer) :
    ''' Creates three layers with the RGB channels of the selected layer.
    
    Parameters:
    img : image The current image.
    layer : layer The layer of the image that is selected.
    '''
    # Indicates that the process has started.
    gimp.progress_init("Discolouring " + layer.name + "...")

    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_image_undo_group_start(img)

    # Get the layer position.
    pos = 0;
    for i in range(len(img.layers)):
        if(img.layers[i] == layer):
            pos = i
            
    # Create the new layers.
    layerR = gimp.Layer(img, layer.name + " Red", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
    layerG = gimp.Layer(img, layer.name + " Green", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
    layerB = gimp.Layer(img, layer.name + " Blue", layer.width, layer.height, layer.type, layer.opacity, layer.mode)
    layerA = gimp.Layer(img, layer.name + " Alpha", layer.width, layer.height, layer.type, layer.opacity, layer.mode)

    img.add_layer(layerR, pos)
    img.add_layer(layerG, pos)
    img.add_layer(layerB, pos)
    img.add_layer(layerA, pos)
    
    # Clear the new layers.
    pdb.gimp_edit_clear(layerR)
    layerR.flush()
    pdb.gimp_edit_clear(layerG)
    layerG.flush()
    pdb.gimp_edit_clear(layerB)
    layerB.flush()
    pdb.gimp_edit_clear(layerA)
    layerA.flush()
    
    # Separate the channels.
    try:
        # Calculate the number of tiles.
        tn = int(layer.width / 64)
        if(layer.width % 64 > 0):
            tn += 1
        tm = int(layer.height / 64)
        if(layer.height % 64 > 0):
            tm += 1
        
        # Iterate over the tiles.
        for i in range(tn):
            for j in range(tm):
                # Update the progress bar.
                gimp.progress_update(float(i*tm + j) / float(tn*tm))
        
                # Get the tiles.
                tile = layer.get_tile(False, j, i)
                tileR = layerR.get_tile(False, j, i)
                tileG = layerG.get_tile(False, j, i)
                tileB = layerB.get_tile(False, j, i)
                tileA = layerA.get_tile(False, j, i)
        
                # Iterate over the pixels of each tile.
                for x in range(tile.ewidth):
                    for y in range(tile.eheight):
                        # Get the pixel and separate his colors.
                        pixel = tile[x,y]
                        pixelR = pixel[0] + pixel[0] +  pixel[0] + "\xff"
                        pixelG = pixel[1] + pixel[1] +  pixel[1] + "\xff"
                        pixelB = pixel[2] + pixel[2] +  pixel[2] + "\xff"
                        pixelA = pixel[3] + pixel[3] +  pixel[3] + "\xff"
                        
                        # Save the value in the channel layers.
                        tileR[x,y] = pixelR
                        tileG[x,y] = pixelG
                        tileB[x,y] = pixelB
                        tileA[x,y] = pixelA
        
        # Update the new layers.
        tileR.flush()
        tileR.merge_shadow(True)
        tileR.update(0, 0, tileR.width, tileR.height)
        tileG.flush()
        tileG.merge_shadow(True)
        tileG.update(0, 0, tileG.width, tileG.height)
        tileB.flush()
        tileB.merge_shadow(True)
        tileB.update(0, 0, tileB.width, tileB.height)
        tileA.flush()
        tileA.merge_shadow(True)
        tileA.update(0, 0, tileA.width, tileA.height)
        
    except Exception as err:
        gimp.message("Unexpected error: " + str(err))
    
    # Close the undo group.
    pdb.gimp_image_undo_group_end(img)
    
    # End progress.
    pdb.gimp_progress_end()

register(
    "python_fu_test_split_channels",
    "Split channels",
    "Creates three layers with the RGB channels of the selected layer.",
    "JFM",
    "Open source (BSD 3-clause license)",
    "2013",
    "<Image>/Filters/Test/Split channels",
    "RGB, RGB*",
    [],
    [],
    split_channels)

main()
