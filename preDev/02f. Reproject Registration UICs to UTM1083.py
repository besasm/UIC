# ---------------------------------------------------------------------------
# 02f. Reproject Registration UICs to UTM1083.py
# Created on: Fri Apr 09 2010 12:47:18 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


# Local variables...
UIC_Registration_Spatial__1_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
Delete_succeeded__1_ = "true"
UIC_Registration_UTM1083 = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial_UTM1083"
UIC_Registration_Spatial_UTM1083__1_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial_UTM1083"

# Process: Delete (1)...
gp.Delete_management(UIC_Registration_Spatial_UTM1083__1_, "FeatureClass")

# Process: Project (1)...
gp.Project_management(UIC_Registration_Spatial__1_, UIC_Registration_UTM1083, "PROJCS['NAD_1983_UTM_Zone_10N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "", "")

