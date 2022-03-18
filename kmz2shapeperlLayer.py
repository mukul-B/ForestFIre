import ogr2ogr


def chc():
    # note: main is expecting sys.argv, where the first argument is the script name
    # so, the argument indices in the array need to be offset by 1

    ogr2ogr.main(["", "-f", "ESRI Shapefile", "heat_20210724_1630.shp", "20210724_1630PDT_Dixie.kmz", "heat"])

if __name__ == '__main__':
    chc()