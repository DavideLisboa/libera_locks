import arcpy
import arcgis.features
from arcgis.gis import GIS
import os
portal = GIS(
    url="https://atlas.caesb.df.gov.br/portal/home/",
    password="PORTAL@dm1n",
    username="portaladmin",
)

fs_url = arcpy.GetParameterAsText(0)
# fs_url = "https://atlas.caesb.df.gov.br/workflow/rest/services/UN_CAESB/CAESB_Utility_Network/FeatureServer"

if fs_url.endswith("FeatureServer"):
    base_url = os.path.dirname(fs_url)
else:
    base_url = os.path.dirname(os.path.dirname(fs_url))


services = ["FeatureServer", "VersionManagementServer"]
service_urls = {url: base_url + '/' + url for url in services}
# The Feature Server (service URL)
version_mgmt_svc = service_urls["VersionManagementServer"]
vms = arcgis.features._version.VersionManager(
    service_urls["VersionManagementServer"], portal)
arcpy.AddMessage(f'Version Management Service: {vms}')

# Find and remove lock(s) for fully qualified version, if exists
for locks in vms.locks:   # use "read" to run start_reading
    vms.purge(locks)
    arcpy.AddMessage(f"Limpado os locks: {locks}")
