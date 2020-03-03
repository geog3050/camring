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
# Given a polygon shapefile with an attribute based on count data (e.g., population, disease count)
# and an areal measurement (square miles, kilometers, or meters):
# this function calculates and appends a new density column to the input shapefile.

# Use a polygon file to do following tasks in your function:
# - Calculate area of each polygon in given input unit (e.g., square miles) and append to a new column
# - Create a field (e.g., density_sqm) and calculate the density of the count variable selected
#   using the area of each polygon and its count variable (e.g., population) 
# 
# 1- Check whether the input variables are correct
#   (e.g., the shape type, attribute name and the areal unit)
# 2- Make sure overwrite is enabled if the field name already exists.
# 3- Give a warning message if the projection is a geographic projection(e.g., WGS84, NAD83).
#    Remember that area calculations are not accurate in geographic coordinate systems. 
# 
###################################################################### 
import system

import arcpy
arcpy.env.workspace = "C:\Users\Cam\Documents\School\2020-2021\Geog3050\Data\assignment2_data"
def calculateDensity(inputShapeFile, attribute, arealUnit):
    desc = arcpy.Describe(inputShapeFile)
        #if desc == polygon:
    return desc

###################################################################### 
# Problem 2 (40 Points)
# 
# Given a line shapefile (e.g.,river_network.shp) and a polygon shapefile (e.g.,states.shp) and a distance unit:
# this function calculates and saves the total length of the line features (e.g., rivers) in given distance unit (e.g., km) for each polygon.
# 
# 1- Check whether the input variables are correct (e.g., the shape types and the distance unit)
# 2- Transform the projection of one to other if the line and polygon shapefiles have different projections
#        
###################################################################### 
def estimateTotalLineLengthInPolygons(inputLineShapeFile, inputClipShapeFile, clipPolygonID, distanceUnit):
    pass

######################################################################
# Problem 3 (30 points)
# 
# Given an input point shapefile, i.e., eu_cities.shp and a distance threshold and unit:
# Calculate the number of points within the distance threshold from each point (e.g., city),
# and append the count to a new field (attribute).
# 
######################################################################
def countObservationsWithinDistance(inputPointShapeFile, distance, distanceUnit):
    pass

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
    print('### Otherwise, the Autograder will assign 0 points.')
