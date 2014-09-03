import arcpy
import os

#this has to be for windows with arcgis installed
folder = 'V:/GIS/data/census/2000'

arcpy.CreateFileGDB_management(folder,"tracts","CURRENT")

def fcs_in_workspace(workspace):
  arcpy.env.workspace = workspace
  for fc in arcpy.ListFeatureClasses():
    yield os.path.join(workspace, fc)
  for ws in arcpy.ListWorkspaces():
    for fc in fcs_in_workspace(os.path.join(workspace, ws)):
        yield fc

fcSet = []
for fc in fcs_in_workspace(folder+'/tracts'):
	fcSet.append(fc.encode('ascii', 'ignore'))
	print fc 

print fcSet

arcpy.Merge_management(fcSet, folder + "/tracts.gdb/tracts_2000")