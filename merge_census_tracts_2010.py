import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

wd = 'W:/GIS/Data/Census/census_2010/tracts'

folder = wd

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

arcpy.Merge_management(fcSet, folder + "/census.gdb/tracts_2010")