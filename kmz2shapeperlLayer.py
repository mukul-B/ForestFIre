from datetime import datetime

import ogr2ogr
import os
import re
import warnings

warnings.filterwarnings('ignore')


def match_file(filename):
    match = re.search(r"(((\d+)_(\d+))PDT_Dixie.km[lz])", filename)
    extract = 2
    if match == None:
        match = re.search(r"(((\d+)_(\d+))PDT_Dixie_IR.km[lz])", filename)

    if match == None:
        match = re.search(r"(((\d+)_(\d+))PDT_DixieNW.km[lz])", filename)

    if match == None:
        match = re.search(r"(((\d+)_(\d+))PDT_DixieSE.km[lz])", filename)

    if match == None:
        match = re.search(r"(((\d+)_(\d+))_Dixie_IR.km[lz])", filename)

    if match == None:
        match = re.search(r"(((\d+)_(\d+))PDT_Dixie - NorthEast_IR.km[lz])", filename)

    if match == None:
        match = re.search(r"(((\d+)_(\d+))PDT_Dixie.km[lz])", filename)

    if match == None:
        match = re.search(r"((\d+)_Dixie_(\d+)PDT_IR.km[lz])", filename)
        extract = 3
    if match == None:
        match = re.search(r"((\d+)_Dixie_IR.km[lz])", filename)
        extract = 4

    if (match == None):
        return None
    else:
        if extract == 2:
            return match.group(2)
        elif extract == 3:
            return match.group(2) + "_" + match.group(3)
        elif extract == 4:
            return match.group(2) + "_0000"



def valid_file(filename):
    match = match_file(filename)
    if match is None:
        print("invalid", filename)
        return False
    try:
        # print(match)
        time = datetime.strptime(match, '%Y%m%d_%H%M%S')
        # print(time)
    except ValueError:
        return False
        # print(time)
    return match


def kmz2shape(source, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
        print("The new directory is created!")
    directory = os.listdir(source)
    non_valid_name = 0
    org_error_files = 0
    success_file = 0
    for filename in directory:
        extract=valid_file(filename)
        if extract:
            # success = ogr2ogr.main(
            #     ["", "-f", "ESRI Shapefile", dest + "/heat_" + filename.replace(".kmz", ".shp"),
            #      source + "/" + filename,
            #      "heat"])
            success = ogr2ogr.main(
                ["", "-f", "ESRI Shapefile", dest + "/heat_" + extract + ".shp",
                 source + "/" + filename,
                 "heat"])
            if not success:
                print(source + "/" + filename)
                org_error_files += 1
                # exit(0)
            else:
                success_file+=1
        else:
            non_valid_name += 1
    print("org_error_files",org_error_files)
    print("non_valid_name",non_valid_name)
    print("success_file", success_file)
    print("total_file", len(directory),org_error_files+ non_valid_name+ success_file)


def filename2time(filename):
    match = re.search(r"(((\d{8})_(\d{4}))PDT_Dixie.kmz)", filename)
    try:
        time = datetime.strptime(match.group(2), '%Y%m%d_%H%M%S')
    except ValueError:
        return False
        # print(time)
    return True


if __name__ == '__main__':
    # print(valid_file("20210906_Dixie_1718PDT_IR.kml"))
    kmz2shape("/home/muku/Downloads/DixiePart1", "shapefiles")
    kmz2shape("/home/muku/Downloads/DixiePart2", "shapefiles")
    kmz2shape("/home/muku/Downloads/DixiePart3", "shapefiles")
    kmz2shape("/home/muku/Downloads/DixiePart4", "shapefiles")
    # 20210908_Dixie_1419PDT_IR.kmz
    # 20210911_1421PDT_Dixie_IR.kmz
