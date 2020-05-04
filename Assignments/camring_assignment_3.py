import arcpy
import os
from arcpy.sa import *

def hawkid():
    return(["Cameron Ring", "camring"])
 
def importCSVIntoGeodatabase(csvFile, geodatabase):
    geodatabasePath = os.path.abspath(geodatabase)
    arcpy.env.workspace= geodatabasePath
    arcpy.env.overwriteOutput = True
    csvFilePath = os.path.abspath(csvFile)
    os.rename(csvFilePath, geodatabasePath+"\\"+csvFile)
          
def krigingFromPointCSV(inTable, valueField, xField, yField, inClipFc, workspace = "assignment3.gdb"):
    folderPath = os.path.abspath(workspace)
    workspace = os.path.dirname(folderPath)
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True
    featureclasses = arcpy.ListFeatureClasses()
    #generating an input feature layer using the input table
    out_layer = str(inTable)+"_lyr"
    out_layerPath = os.path.abspath(out_layer)
    arcpy.MakeXYEventLayer_management(inTable, xField, yField, out_layer)

    #converting projection to clip layer
    out_layerDesc = arcpy.Describe(out_layer)
    clip_desc = arcpy.Describe(inClipFc)
    if out_layerDesc.spatialReference.name != clip_desc.spatialReference.name:
        arcpy.Project_management(out_layer,"out_layer_proj", str(clip_desc.spatialReference.name))
    #Kriging Model with projection
        lagSize = 70000
        majorRange = 250000
        partialSill = 180000
        nugget = 34000
        arcpy.CheckOutExtension("Spatial")
        inPointFeature = "out_layer_proj"
        outVarRaster = workspace+"\\ovariance2"
        kModelOrdinary = KrigingModelOrdinary("Circular", lagSize, majorRange, partialSill, nugget)
        outKrigingOrd2 = Kriging(inPointFeature, valueField, kModelOrdinary, 2000, RadiusFixed(200000, 10), outVarRaster)
        outKrigingOrd2.save(outVarRaster)

    #Kriging Model without projection
    elif out_layerDesc.spatialReference.name == clip_desc.spatialReference.name:
        lagSize = 70000
        majorRange = 250000
        partialSill = 180000
        nugget = 34000
        arcpy.CheckOutExtension("Spatial")
        inPointFeature = out_layer
        outVarRaster = workspace+"\\ovariance2"
        kModelOrdinary = KrigingModelOrdinary("Circular", lagSize, majorRange, partialSill, nugget)
        outKrigingOrd2 = Kriging(inPointFeature, valueField, kModelOrdinary, 2000, RadiusFixed(200000, 10), outVarRaster)
        outKrigingOrd2.save(outVarRaster)                     
    outExtractByMask = ExtractByMask(outVarRaster, inClipFc, workspace+"\\ovariance2_clip.shp")
    outExtractByMask.save(workspace+"\\ovariance2_clip.shp")
    #removing old raster 
    os.remove(outVarRaster)
    
    

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
