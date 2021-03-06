# ---------------------------------------------------------------------------
# 01. DataRefresh old.py
# Created on: Tue Apr 16 2013 05:24:42 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


# Local variables...
UIC_Registration_Spatial__6_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"
Delete_succeeded__4_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"
UIC_Registration_Spatial__4_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"
Manual_Surface_Subcatchment_Delineations = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_tempSSCs"
UIC_Registration_Spatial__5_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_tempSSCs__2_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_tempSSCs"
UIC_Registration_tempSSCs__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_tempSSCs"
Delete_succeeded__5_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_tempSSCs"
UIC_Registration_temp_Projected__5_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_temp_Projected"
UIC_Registration_temp__2_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_temp"
UIC_Registration_Spatial__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_temp_Projected__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_temp_Projected"
UIC_Registration_temp_Projected__6_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_temp_Projected"
UIC_Registration_temp_Projected__7_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_temp_Projected"
UIC_Registration_Spatial__2_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_Spatial__3_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
Delete_succeeded__3_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_temp_Projected"
UIC_Registration__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration"
Delete_succeeded__1_ = "true"
Delete_succeeded__2_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Registration.mdb\\UIC_Registration_temp"
UIC_Registration_Layer__1_ = "UIC_Registration_Layer"
UIC_Registration_Spatial = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"

# Process: Make XY Event Layer...
gp.MakeXYEventLayer_management(UIC_Registration__1_, "longDD", "latDD", UIC_Registration_Layer__1_, "")

# Process: Delete (1)...
gp.Delete_management(UIC_Registration_Spatial__1_, "FeatureClass")

# Process: Copy Features (2)...
gp.CopyFeatures_management(UIC_Registration_Layer__1_, UIC_Registration_temp__2_, "", "0", "0", "0")

# Process: Project (1)...
gp.Project_management(UIC_Registration_temp__2_, UIC_Registration_temp_Projected__1_, "PROJCS['NAD_1983_HARN_StatePlane_Oregon_North_FIPS_3601',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',8202099.737532808],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',44.33333333333334],PARAMETER['Standard_Parallel_2',46.0],PARAMETER['Latitude_Of_Origin',43.66666666666666],UNIT['Foot',0.3048]]", "", "")

# Process: Add XY Coordinates...
gp.AddXY_management(UIC_Registration_temp_Projected__1_)

# Process: Calculate longFeet...
gp.CalculateField_management(UIC_Registration_temp_Projected__5_, "longFeet", "[POINT_X]", "VB", "")

# Process: Calculate latFeet...
gp.CalculateField_management(UIC_Registration_temp_Projected__6_, "latFeet", "[POINT_Y]", "VB", "")

# Process: Copy (3)...
gp.Copy_management(UIC_Registration_temp_Projected__7_, UIC_Registration_Spatial__2_, "")

# Process: Delete Field (1)...
gp.DeleteField_management(UIC_Registration_Spatial__2_, "POINT_X;POINT_Y")

# Process: Delete (4)...
gp.Delete_management(UIC_Registration_Spatial__4_, "FeatureClass")

# Process: Copy (4)...
gp.Copy_management(UIC_Registration_Spatial__5_, UIC_Registration_Spatial__6_, "FeatureClass")

# Process: Delete (5)...
gp.Delete_management(UIC_Registration_tempSSCs__1_, "FeatureClass")

# Process: Copy (5)...
gp.Copy_management(UIC_Registration_tempSSCs__2_, Manual_Surface_Subcatchment_Delineations, "FeatureClass")

# Process: Delete (3)...
gp.Delete_management(UIC_Registration_temp_Projected__7_, "")

# Process: Delete (2)...
gp.Delete_management(UIC_Registration_temp__2_, "")

# Process: Add Field...
gp.AddField_management(UIC_Registration_Spatial__6_, "altRegID", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

