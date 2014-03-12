import arcpy
import os

#this has to be for windows with arcgis installed
folder = 'U:/GIS/data/blocks'

arcpy.CreateFileGDB_management(folder,"census","CURRENT")

def fcs_in_workspace(workspace):
  arcpy.env.workspace = workspace
  for fc in arcpy.ListFeatureClasses():
    yield os.path.join(workspace, fc)
  for ws in arcpy.ListWorkspaces():
    for fc in fcs_in_workspace(os.path.join(workspace, ws)):
        yield fc

fcSet = []
for fc in fcs_in_workspace(folder):
	fcSet.append(fc.encode('ascii', 'ignore'))
	print fc 

print fcSet

arcpy.Merge_management(fcSet, folder + "/census.gdb/blocks_2000")