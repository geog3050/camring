import arcpy
import os
arcpy.env.overwriteOutput = True
def findVarDiff(shpfile ="census_2010_county_DP1.shp",
                    inTable ="C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\unemploymet_rate_data.csv",
                    varBef="unem_rate_2010",
                    varAfter="unem_rate_2018",
                    varChange ="unem_change",
                    inField ="NAMELSAD10",
                    joinField ="GeographicAreaName",
                    workspace ="C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject"):

    #ShpFile: the initial shapefile where you want to compare two variables
    #inTable: the csv or txt file that containes the fields you want to compare
    #varBef: the field you're subtracting from
    #varAfter: field to be subtracted
    #varChange: The name of the field where you want to put the differences
    #inField: the field that is going to be joined to
    #joinField: The field that joins to the inField
    #workspace: where this is all happening
    
    arcpy.env.workspace = workspace
    #creates a gdb file to work in
    out_folder_path = workspace
    out_name = "VarDif.gdb"
    arcpy.CreateFileGDB_management(out_folder_path, out_name)

    #add xcell file to the gdb
    inTable = inTable
    gdbLocation = workspace + "\\" +"VarDif.gdb"
    outTable = "Difdata"
    arcpy.TableToTable_conversion(inTable, gdbLocation, outTable)

    #copying shpfile to gdb
    shpfilePath = os.path.abspath(shpfile)
  
    inFeatures = [shpfilePath]
 
    arcpy.FeatureClassToGeodatabase_conversion(inFeatures, gdbLocation)


    #joinging the table to the feature class
    arcpy.env.workspace = gdbLocation

    inFeature = gdbLocation + "\\" + str(shpfile)
    inField = inField
    joinTable = "Difdata"
    joinField = joinField

    arcpy.JoinField_management(inFeature, inField, joinTable, joinField)


    gdbShape = inFeature
    #create a new field for low & high populations
    inTable = gdbShape
    field_name = "dev_lev"
    field_type = "TEXT"
    arcpy.AddField_management(inTable, field_name, field_type)

    #Third field for change in unemployment
    field_name2 = varChange
    field_type2 = "DOUBLE"
    arcpy.AddField_management(inTable, field_name2, field_type2)

    #sort above or below 50000 pop & change of unem_rate into new fields using update cursor
    fc = gdbLocation + "\\"+ "census_2010_county_DP1"

    updatecursor = arcpy.da.UpdateCursor(fc, ["DP0010001", "dev_lev", varBef, varAfter, varChange])
    for row in updatecursor:
        if row[0] >= 50000:
            row[1] = "Urban"
        elif row[0] < 50000:
            row[1] = "Rural"
        row[4] = row[3] - row[2]
        updatecursor.updateRow(row)
    del row
    del updatecursor

    #Make a layer containing positive changes in unemployment
    arcpy.MakeFeatureLayer_management(fc, "posChange_lyr", str(varChange)+" > 0")
    
    #clip and make a new layer with thos values/ create a new fc from layer
    arcpy.CopyFeatures_management("posChange_lyr", gdbLocation+"\\"+"posChange")



