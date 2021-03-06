# ---------------------------------------------------------------------------
# 10. CalcProxtoECSI.py
# Created on: Tue Apr 16 2013 05:32:21 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
ECSI_Sites_Feature_Layer__1_ = "ECSI_Sites_FeatureLayer"
UIC_Registration_near_ECSI__3_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"
UIC_Registration_near_ECSI__5_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"
UIC_Registration_near_ECSI = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"
ECSI_Sites_on_CGIS__1_ = "Database Connections\\egh_public.sde\\EGH_PUBLIC.ARCMAP_ADMIN.ecsi_sites_bes_pdx"
UIC_Registration_near_ECSI__2_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"
UIC_Registration_Spatial__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"
UIC_Registration_near_ECSI__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"
Delete_succeeded__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"
UIC_Registration_near_ECSI__6_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"
UIC_Registration_near_ECSI__7_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_near_ECSI"

# Process: Delete (1)...
gp.Delete_management(UIC_Registration_near_ECSI__1_, "FeatureClass")

# Process: Copy Features (1)...
gp.CopyFeatures_management(UIC_Registration_Spatial__1_, UIC_Registration_near_ECSI__2_, "", "0", "0", "0")

# Process: Make Feature Layer (1)...
gp.MakeFeatureLayer_management(ECSI_Sites_on_CGIS__1_, ECSI_Sites_Feature_Layer__1_, "", "", "ID ID VISIBLE NONE;SITE_ID SITE_ID VISIBLE NONE;SITE_NAME SITE_NAME VISIBLE NONE;ADDRESS ADDRESS VISIBLE NONE;CITY_NAME CITY_NAME VISIBLE NONE;ZIP_CODE ZIP_CODE VISIBLE NONE;COUNTY COUNTY VISIBLE NONE;CODE CODE VISIBLE NONE;STATUS STATUS VISIBLE NONE;LATITUDE LATITUDE VISIBLE NONE;LONGITUDE LONGITUDE VISIBLE NONE;GEO_TL GEO_TL VISIBLE NONE;GEO_CL GEO_CL VISIBLE NONE;GEO_NO GEO_NO VISIBLE NONE;BES_LON BES_LON VISIBLE NONE;BES_LAT BES_LAT VISIBLE NONE;BES_NAD83X BES_NAD83X VISIBLE NONE;BES_NAD83Y BES_NAD83Y VISIBLE NONE;DIFF_FEET DIFF_FEET VISIBLE NONE;COMMENTS COMMENTS VISIBLE NONE")

# Process: Near (1)...
gp.Near_analysis(UIC_Registration_near_ECSI__2_, "ECSI_Sites_FeatureLayer", "", "NO_LOCATION", "NO_ANGLE")

# Process: Add Field (2)...
gp.AddField_management(UIC_Registration_near_ECSI__3_, "nearECSIObjID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (1)...
gp.CalculateField_management(UIC_Registration_near_ECSI__6_, "nearECSI", "[NEAR_DIST]", "VB", "")

# Process: Calculate Field (2)...
gp.CalculateField_management(UIC_Registration_near_ECSI__5_, "nearECSIObjID", "[NEAR_FID]", "VB", "")

# Process: Delete Field (1)...
gp.DeleteField_management(UIC_Registration_near_ECSI__7_, "NEAR_FID;NEAR_DIST")

