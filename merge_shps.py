# merge_shps.py
import os

path = ""  # path to your folder of .shp files
merge = "merge_filename"                         # this will be the name of your merged result

# directory = os.listdir(path)

count = 0
# for filename in directory:
for i in range(1):

    filename="heat_20210724_1630.shp"
    if ".SHP" in filename.upper() and not ".XML" in filename.upper():

        # On the first pass, create a clone and add the filename column.
        if count == 0:
            # Make a clone (matt wilkie)..
            # cmd = 'ogr2ogr ' + path + '/' + merge + '.shp ' + path + '/' + filename + ' -where "FID < 0"'
            cmd = 'ogr2ogr ' + merge + '.shp ' + filename + ' -where "FID < 0"'
            print(cmd)
            os.system(cmd)

            # Add the field (j03lar50n)..
            # cmd = 'ogrinfo ' + path + '/' + merge + '.shp -sql "ALTER TABLE ' + merge + ' ADD COLUMN filename character(50)"'
            cmd = 'ogrinfo ' + merge + '.shp -sql "ALTER TABLE ' + merge + ' ADD COLUMN filename character(50)"'

            print(cmd)
            os.system(cmd)

        # Now populate the data (capooti)..
        print("Merging: " + str(filename))

        # You'll need the filename without the .shp extension for the OGR_SQL..
        filenameNoExt = filename.replace(".shp","")

        # cmd = 'ogr2ogr -f "esri shapefile" -update -append ' + \
        #         path + '/' + merge + '.shp ' + \
        #         path + '/' + filename + \
        #         ' -sql "SELECT \'' + filename + '\' AS filename, * FROM ' + filenameNoExt + '"'
        cmd = 'ogr2ogr -f "esri shapefile" -update -append ' + \
               merge + '.shp ' + \
              filename + \
              ' -sql "SELECT \'' + filename + '\' AS filename, * FROM ' + filenameNoExt + '"'
        # Uncomment this line to spit the ogr2ogr sentence to the terminal..
        #print "\n" + cmd + "\n"
        print(cmd)
        os.system(cmd)

        count += 1
