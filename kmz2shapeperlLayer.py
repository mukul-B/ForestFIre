import ogr2ogr


def chc():
    # note: main is expecting sys.argv, where the first argument is the script name
    # so, the argument indices in the array need to be offset by 1

    ogr2ogr.main(
        ["", "-f", "ESRI Shapefile", "shapefiles/heat_20210724_1630.shp", "20210724_1630PDT_Dixie.kmz", "heat"])
    ogr2ogr.main(
        ["", "-f", "ESRI Shapefile", "shapefiles/heat_20210724_1945.shp", "20210724_1945PDT_Dixie.kmz", "heat"])
    ogr2ogr.main(
        ["", "-f", "ESRI Shapefile", "shapefiles/heat_20210724_2300.shp", "20210724_2300PDT_Dixie.kmz", "heat"])
    ogr2ogr.main(
        ["", "-f", "ESRI Shapefile", "shapefiles/heat_20210725_1430.shp", "20210725_1430PDT_Dixie.kmz", "heat"])


if __name__ == '__main__':
    chc()
