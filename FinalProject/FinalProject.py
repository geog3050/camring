import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\census_2010_county_DP1"


#creates a gdb file to work in
out_folder_path = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject"
out_name = "final.gdb"
arcpy.CreateFileGDB_management(out_folder_path, out_name)

#add xcell file to the gdb
inTable = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\unemploymet_rate_data.csv"
outLocation = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\final.gdb"
outTable = "final_data"
arcpy.TableToTable_conversion(inTable, outLocation, outTable)

#copying shpfile to gdb
inFeatures = ["census_2010_county_DP1.shp"]
outLocation = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\final.gdb"
 
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)


#joinging the table to the feature class
arcpy.env.workspace = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\final.gdb"

inFeature = "census_2010_county_DP1"
inField = "NAMELSAD10"
joinTable = "final_data"
joinField = "GeographicAreaName"

arcpy.JoinField_management(inFeature, inField, joinTable, joinField)



#create a new field for low & high populations
inTable = "census_2010_county_DP1"
field_name = "dev_lev"
field_type = "TEXT"
arcpy.AddField_management(inTable, field_name, field_type)

#Third field for change in unemployment
field_name2 = "unem_change"
field_type2 = "DOUBLE"
arcpy.AddField_management(inTable, field_name2, field_type2)

#sort above or below 50000 pop & change of unem_rate into new fields using update cursor
fc = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\final.gdb\\census_2010_county_DP1"
#field_names = [f.name for f in arcpy.ListFields(fc)]
#print(field_names)
updatecursor = arcpy.da.UpdateCursor(fc, ["DP0010001", "dev_lev", "unem_rate_2010", "unem_rate_2018", "unem_change"])
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
arcpy.MakeFeatureLayer_management("census_2010_county_DP1", "posChange_lyr", "unem_change > 0")
#clip and make a new layer with thos values/ create a new fc from layer
arcpy.CopyFeatures_management("posChange_lyr", "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\final.gdb")



