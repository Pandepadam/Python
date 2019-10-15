import arcpy
mxd = arcpy.mapping.MapDocument()
mapLyr1 = arcpy.mapping.ListLayers(mxd, "text_points") [0]

feature_info = list()
