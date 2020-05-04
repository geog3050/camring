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

##################################################################################################### 
# 100 Points Total
#
# Given a linear shapefile (roads) and a point shapefile representing facilities(schools),
# this function should generate either a time-based (1-,2-,3- minute) or road network distance-based (200-, 400-, 600-, .. -2000 meters)
# concentric service areas around facilities and save the results to a layer file on an output geodatabase.
# Although you are not required to map the result, make sure to check your output service layer feature.
# The service area polygons can be used to visualize the areas that do not have adequate coverage from the schools. 

# Each parameter is described below:

# inFacilities: The name of point shapefile (schools)     
# roads: The name of the roads shapefile
# workspace: The workspace folder where the shapefiles are located. 

# Below are suggested steps for your program. More code may be needed for exception handling
# and checking the accuracy of the input values.

# 1- Do not hardcode any parameters or filenames in your code.
#    Name your parameters and output files based on inputs. 
# 2- Check all possible cases where inputs can be in wrong type, different projections, etc. 
# 3- Create a geodatabase using arcpy and import all initial shapefiles into feature classes. All your processes and final output should be saved into
#    the geodatabase you created. Therefore, set the workspace parameter to the geodatabase once it is created.
# 4- Using the roads linear feature class, create and build a network dataset. Check the Jupyter notebook shared on ICON,
#    which covers the basics of how to create and build a network dataset from scratch. 
# 5- Use arcpy's MakeServiceAreaLayer function in the link below:
#    https://pro.arcgis.com/en/pro-app/tool-reference/network-analyst/make-service-area-layer.htm
#    Specify the following options while creating the new service area layer. Please make sure to read all the parameters needed for the function. 
#       If you use "length" as impedance_attribute, you can calculate concentric service areas using 200, 400, 600, .. 2000 meters for break values.
#       Feel free to describe your own break values, however, make sure to include at least three of them. 
#       Generate the service area polygons as rings, so that anyone can easily visualize the coverage for any given location if needed.
#       Use overlapping polygons to determine the number of facilities (schools) that cover a given location.
#       Use hierarchy to speed up the time taken to create the polygons.
#       Use the following values for the other parameters:
#       "TRAVEL_FROM", "DETAILED_POLYS", "MERGE"
#################################################################################################################### 
import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("network")
def calculateNetworkServiceArea(inFacilities, roads, workspace):
    #beginning workspace
    arcpy.env.workspace = workspace
    
    #checking correct fc for network analysis
    featureclasses = arcpy.ListFeatureClasses()
    fc1 = featureclasses[0]
    fc2 = featureclasses[1]
    describe_fc1 = arcpy.Describe(fc1)
    describe_fc2 = arcpy.Describe(fc2)
    if describe_fc2.shapeType != "Point":
        return(describe_fc2.shapeType)
        return("Wrong shapefile type for facilities.")

    if describe_fc1.shapeType != "Polyline":
        return(describe_fc1.shapeType)
        return("Wrong shapefile type for network.")


    # creates a gdb file for analysis
    arcpy.CreateFileGDB_management(workspace, "Net_Analysis.gdb")
    #path of gdb file
    gdb_workspace = os.path.abspath(workspace) + "\\Net_Analysis.gdb"
    #setting workspace to the new gdb file
    arcpy.env.workspace = gdb_workspace
    
    out_name = "net_analysis"
    folderPath = os.path.abspath(workspace)
    dsc_fc = arcpy.Describe(roads)
    coord_sys = dsc_fc.spatialReference

    
    arcpy.CreateFeatureDataset_management("Net_Analysis.gdb", out_name, coord_sys)
    arcpy.CopyFeatures_management(folderPath + "\\" + str(roads), gdb_workspace)
    arcpy.CopyFeatures_management(folderPath + "\\" + str(inFacilities), gdb_workspace)

    arcpy.na.CreateNetworkDataset("net_analysis", "route_ND", ["roads"])

    
    arcpy.na.MakeServiceAreaAnalysisLayer("net_analysis//roads_ND", layer_name="an_layer", travel_mode="Driving Time", travel_direction="FROM_FACILITIES",
                                          cutoffs="5;10;15", time_of_day="", time_zone="", output_type="POLYGONS", polygon_detail="STANDARD",
                                          geometry_at_overlaps="OVERLAP", geometry_at_cutoffs="RINGS", polygon_trim_distance="100 Meters", exclude_sources_from_polygon_generation="",
                                          accumulate_attributes="")

    
    arcpy.na.AddLocations("an_layer", "Facilities", "net_analysis\schools", field_mappings="Name Name #",
                          search_tolerance="5000 Meters", sort_field="", search_criteria="",
                          match_type="MATCH_TO_CLOSEST", append="APPEND", snap_to_position_along_network="NO_SNAP", snap_offset="5 Meters",
                          exclude_restricted_elements="EXCLUDE", search_query="")

    arcpy.na.Solve("an_layer", ignore_invalids="SKIP", terminate_on_solve_error="TERMINATE",
                   simplification_tolerance="", overrides="")
    
    
######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
