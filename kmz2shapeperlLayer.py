import ogr2ogr
import os
import re
import warnings
warnings.filterwarnings('ignore')




def valid_file(filename):
    match = re.search(r"((\d+)_(\d+)PDT_Dixie.kmz)", filename)
    return match is not None


def kmz2shape(source, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
        print("The new directory is created!")
    directory = os.listdir(source)
    non_valid_name=0
    org_error_files=0
    for filename in directory:
        if(valid_file(filename)):
            # print(source + "/" + filename)

             success= ogr2ogr.main(
                    ["", "-f", "ESRI Shapefile", dest + "/heat_" + filename.replace(".kmz", ".shp"),
                     source + "/" + filename,
                     "heat"])
             if not success:
                print(source + "/" + filename)
                org_error_files+=1
                # exit(0)
    print(org_error_files)

if __name__ == '__main__':
    kmz2shape("/home/muku/Downloads/DixiePart1", "shapefiles")
