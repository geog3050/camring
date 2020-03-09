###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Cameron Ring", "camring"])

###################################################################### 
# Problem 1 (30 Points)
#
# Given a polygon feature class in a geodatabase, a count attribute of the feature class(e.g., population, disease count):
# this function calculates and appends a new density column to the input feature class in a geodatabase.

# Given any polygon feature class in the geodatabase and a count variable:
# - Calculate the area of each polygon in square miles and append to a new column
# - Create a field (e.g., density_sqm) and calculate the density of the selected count variable
#   using the area of each polygon and its count variable(e.g., population) 
# 
# 1- Check whether the input variables are correct(e.g., the shape type, attribute name)
# 2- Make sure overwrite is enabled if the field name already exists.
# 3- Identify the input coordinate systems unit of measurement (e.g., meters, feet) for an accurate area calculation and conversion
# 4- Give a warning message if the projection is a geographic projection(e.g., WGS84, NAD83).
#    Remember that area calculations are not accurate in geographic coordinate systems. 
# 
###################################################################### 
import sys
import arcpy
#setting workspace
folderpath = os.path.abspath("assignment2.gdb")
workspace = os.path.dirname(folderpath)
arcpy.env.workspace = workspace
def calculateDensity(fcpolygon, attribute, geodatabase = "assignment2.gdb"):
    #finding workspace in current directory 
    arcpy.env.workspace = os.path.abspath(geodatabase)
    #variables
    featureClasses = arcpy.ListFeatureClasses()
    describe_fcpolygon = arcpy.Describe(fcpolygon)
    dist_mes = describe_fcpolygon.spatialReference.LinearUnitName
    geo_sys = describe_fcpolygon.spatialReference.name

    #1. checking fcpolygon input variable
    describe_fc = arcpy.Describe(fcpolygon)
    if describe_fc.shapeType != "Polygon":
        return("fc not a polygon.")

    #1. checking attribute
    field_names = [f.name for f in arcpy.ListFields(fcpolygon)]
    for item in field_names:
        if attribute not in field_names:
            return("Wrong attribute name.")

    #create a field for area and density (make sure overite enabled)
    fields = arcpy.ListFields("area_sqm", "density_sm")
    try:
        arcpy.AddField_management(fcpolygon, "area_sqm", "FLOAT")
        arcpy.AddField_management(fcpolygon, "density_sqm, "FLOAT")
    except:
        arcpy.DeleteField_management(fcpolygon,["area_sqm", "density_sqm"])
        if len(fields) <= 2:
            arcpy.AddField_management(fcpolygon, "area_sqm", "FLOAT")
            arcpy.AddField_management(fcpolygon, "density_sqm, "FLOAT")
        

        
    #calculating area and updateing area in sqm
    #UpdateCursor = arcpy.da.UpdateCursor(fcpolygon, ["Shape_Area", "area_sqm"])
    #for row in UpdateCursor:
        #if dist_mes == "Meter":
            #row[1] = row[0] * 0.0000003861
        #else:
            #row[1] = row[0]
        #UpdateCursor.updateRow(row)
    #del row
    #del UpdateCursor
                              
    #creating an update cursor to do density in sqm
    
    UpdateCursor = arcpy.da.UpdateCursor(fcpolygon, ["area_sqm", attribute, "density_sqm"])
    for row in UpdateCursor:
        row[0] = arcpy.CalculateGeometryAttributs(fcPolygon,["AREA", "SQUARE_MILES_US"] 
        row[2] = row[1]/row[0]
        UpdateCursor.updateRow(row)
    del row
    del UpdateCursor

    
    #warning for geographic coordinate system
    if geo_sys == "GCS_WGS_1984" or geo_sys != None:
        print("warning area calculations are not accurate in geographic coordinate systems.")
    #return message


###################################################################### 
# Problem 2 (40 Points)
# 
# Given a line feature class (e.g.,river_network.shp) and a polygon feature class (e.g.,states.shp) in a geodatabase, and
# a specific id or name of a single polygon (e.g., Iowa) for using as a clip feature:
# this function clips the linear feature class by the selected polygon boundary,
# and then calculates and returns the total length of the line features (e.g., rivers) in miles for the selected polygon.
# 
# 1- Check whether the input variables are correct (e.g., the shape types and the name or id of the selected polygon)
# 2- Transform the projection of one to other if the line and polygon shapefiles have different projections
# 3- Identify the input coordinate systems unit of measurement (e.g., meters, feet) for an accurate distance calculation and conversion
#        
###################################################################### 
def estimateTotalLineLengthInPolygons(fcLine, fcClipPolygon, clipPolygonID, geodatabase = "assignment2.gdb"):
    #variables
    total_dist = 0.0
    field_name = clipPolygonID
    arcpy.AddField_management(fcClipPolygon, field_name, "FLOAT")
     
    #checking input variables

    #determinining & changing projection
    
    #calculating total distance
    cursor = arcpy.da.UpdateCursor(fcClipPolygon,["NAMELSAD10", field_name])
    for row in cursor:
        if row[0] == clipPolygonID:
            arcpy.Intersect_analysis([fcLine] "fcLine_intersect", "ALL", "","LINE")
    del row
    del cursor

    cursor = arcpy.da.SearchCursor(fcLine_intersect,["SHAPE@LENGTH"]) 
    for row in cursor:
        return(row[0])
    del row
    del cursor

######################################################################
# Problem 3 (30 points)
# 
# Given an input point feature class, (i.e., eu_cities.shp) and a distance threshold and unit:
# Calculate the number of points within the distance threshold from each point (e.g., city),
# and append the count to a new field (attribute).
#
# 1- Identify the input coordinate systems unit of measurement (e.g., meters, feet, degrees) for an accurate distance calculation and conversion
# 2- If the coordinate system is geographic (latitude and longitude degrees) then calculate bearing (great circle) distance
#
######################################################################
def countObservationsWithinDistance(fcPoint, distance, distanceUnit, geodatabase = "assignment2.gdb"):
    cursor = arcpy.da.SearchCursor(fcPoint, ["ObjectID"])
    for row in cursor:
        arcpy.PointDistance_analysis(row[0], fcPoint, out_table, distance)
    return(out_table)
    

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
    print('### Otherwise, the Autograder will assign 0 points.')
