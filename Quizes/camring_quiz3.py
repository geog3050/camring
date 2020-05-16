import sys
import arcpy
arcpy.env.workspace = r"C:\Users\Cam\Documents\School\2020-2021\Geog3050\Data\Quiz_3\airports"
arcpy.env.overwriteOutput = True
featureclasses = arcpy.ListFeatureClasses()
fc = featureclasses[0]

seaplane = ["Seaplane Base"]
airport = ["Airport"]
#field_names = [f.name for f in arcpy.ListFields(fc)]
#creating a new field to hold distances for buffer
arcpy.AddField_management(fc, "buff_dist", "STRING")
#update cursor to set new field to distance depending on the string the row contains
updatecursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "buff_dist"])
for row in updatecursor:
    if row[0] in seaplane:
        row[1] = "7500 Meter"
    elif row[0] in airport:
        row[1] = "15000 Meter"
    else:
        print("error")
    updatecursor.updateRow(row)
del row
del updatecursor
    
#print(field_names)    
#searchcursor = arcpy.da.SearchCursor(fc, ["Feature", "buff_dist"])
#for row in searchcursor:
    #print(row[1])
#del row
#del searchcursor

#running the buffer function with the field distances
arcpy.Buffer_analysis(fc, r"C:\Users\Cam\Documents\School\2020-2021\Geog3050\Data\Quiz_3\airports\buffer_airports.shp", "buff_dist")
