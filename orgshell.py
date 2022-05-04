import os


def merge2shape(source,destination):
    # destination=dest + '/' + merge + '.shp'
    # source=path + '/' + filename
    cmd = 'ogr2ogr ' + destination + ' ' + source + ' -where "FID < 0"'
    # print(cmd)
    os.system(cmd)


def add_field_in_shape(destination, merge,fieldname,type='INTEGER'):
    # destination = dest + '/' + merge + '.shp'
    cmd = 'ogrinfo ' + destination + ' -sql "ALTER TABLE ' + merge + ' ADD COLUMN ' + fieldname + ' ' + type + '"'
    # print(cmd)
    os.system(cmd)


def add_value_field(source,destination, filename,fieldname,d):
    # destination = dest + '/' + merge + '.shp'
    # source = path + '/' + filename
    filenameNoExt = filename.replace(".shp", "")
    # cmd = 'ogr2ogr -f "esri shapefile" -update -append ' + \
    #       destination + ' ' + \
    #       source + \
    #       ' -sql "SELECT *, \'' + str(int(d.timestamp())) + '\' AS ' + fieldname + ', \'' + str(d.date()) + '\' as timeinHM' +' FROM ' + filenameNoExt + '"'
    cmd = 'ogr2ogr -f "esri shapefile" -update -append ' + \
          destination + ' ' + \
          source + \
          ' -sql "SELECT *, \'' + str(int(d.timestamp())) + '\' AS ' + fieldname + ', \'' + str(d.time()) + '\' as fileHM' +  ' , SUBSTR(descriptio,7,5)  as fieldHM' + ' FROM ' + filenameNoExt + '"'

    print(cmd)
    os.system(cmd)
