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

#sort above or below 50000 pop into new fields using update cursor
fc = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\final.gdb\\census_2010_county_DP1"
updatecursor = arcpy.da.UpdateCursor(fc, ["DP0010001", "dev_lev"])
for row in updatecursor:
    if row[0] >= 50000:
        row[1] = "Urban"
    elif row[0] < 50000:
        row[1] = "Rural"
    updatecursor.updateRow(row)
del row
del updatecursor

#Local bivariate relationship tool to extract data from the relationship of urban and rural employment in Iowa
dep_var = "rate_2010"
expl_var = "DP0010001"
out_ws = "C:\\Users\\Cam\\Documents\\GitHub\\camring\\FinalProject\\final.gdb"
out_name = "LBR_fin"
out_path = os.path.join(out_ws, out_name)

arcpy.LocalBivariateRelationships_stats(fc, dep_var, expl_var, out_path) 

