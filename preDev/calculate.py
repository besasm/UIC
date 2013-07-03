# ---------------------------------------------------------------------------
# calculate.py
# Created on: Thu Apr 08 2010 05:39:39 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


# Local variables...
uic = "C:\\temp\\uic.mdb\\uic"
uic__2_ = "C:\\temp\\uic.mdb\\uic"

# Process: Calculate Field...
gp.CalculateField_management(uic, "DepthText", "round([DEPTH],0)", "PYTHON", "")
