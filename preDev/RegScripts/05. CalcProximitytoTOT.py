# ---------------------------------------------------------------------------
# 05. CalcProximitytoTOT.py
# Created on: Tue Apr 16 2013 05:28:25 PM
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
Two_year_TOT__1_ = "Database Connections\\egh_public.sde\\EGH_PUBLIC.ARCMAP_ADMIN.uic_2yrtot_bes_pdx"
UIC_Registration_in_2yrToT = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_in_2yrToT"
UIC_Registration_temp__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_temp"
UIC_Registration_Spatial__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"
UIC_Registration_in_2yrTOT__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_in_2yrToT"
Delete_succeeded__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_in_2yrToT"
Delete_succeeded__2_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_temp"

# Process: Delete (1)...
gp.Delete_management(UIC_Registration_in_2yrTOT__1_, "FeatureClass")

# Process: Copy Features (1)...
gp.CopyFeatures_management(UIC_Registration_Spatial__1_, UIC_Registration_temp__1_, "", "0", "0", "0")

# Process: Identity (1)...
gp.Identity_analysis(UIC_Registration_temp__1_, Two_year_TOT__1_, UIC_Registration_in_2yrToT, "ONLY_FID", "", "NO_RELATIONSHIPS")

# Process: Delete (2)...
gp.Delete_management(UIC_Registration_temp__1_, "FeatureClass")

