import arcpy


aprx = arcpy.mp.ArcGISProject(
    r"C:\Users\Davil\Documents\ArcGIS\Projects\MyProject9\MyProject9.aprx")
for m in aprx.listMaps():
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)
print("Layouts:")
for lyt in aprx.listLayouts():
    print(f"  {lyt.name} ({lyt.pageHeight} x {lyt.pageWidth} {lyt.pageUnits})")
