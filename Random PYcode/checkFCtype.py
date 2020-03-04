import sys
import arcpy
#workspace where shape file is
arcpy.env.workspace = "C:\Users\camring\Geog3050\data\Assignment2"
#listing fc
featureclasses = arcpy.ListFeatureClasses()
#setting fc
fc = featureclasses[1]

describe_fc = arcpy.Describe(fc)
#checking if they're similar
if describe_fc.shapeType == "Polygon":
    print('This is a polygon shapefile')
elif describe_fc.shapeType == "Polyline":
    print('This is a polyline shapefile')
elif describe_fc.shapeType == "Point":
    print('this is a point')
else:
    print("Type unkown")

GeoRef = describe_fc.spatialReference.name
if GeoRef == "GCS_WGS_1984":
    print("Calc not accurate in geo coordinate system")
