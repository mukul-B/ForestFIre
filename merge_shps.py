import os
import re
from datetime import datetime
import orgshell


def filename2time(filename):
    match = re.search(r"_((\d+)_(\d+))", filename)
    time = datetime.strptime(match.group(1), '%Y%m%d_%H%M%S')
    # print(time)
    return time


path = "shapefiles"  # path to your folder of .shp files
merge = "merge_filename"  # this will be the name of your merged result
dest = "merged"

if not os.path.exists(dest):
    os.makedirs(dest)
    # print("The new directory is created!")

directory = os.listdir(path)

count = 0

for filename in directory:

    if ".SHP" in filename.upper() and not ".XML" in filename.upper():
        destination = dest + '/' + merge + '.shp'
        source = path + '/' + filename

        if count == 0:
            orgshell.merge2shape(source, destination)
            orgshell.add_field_in_shape(destination, merge,"timeinint")

        d = filename2time(filename)
        orgshell.add_value_field(source, destination, filename,"timeinint", d)
        count += 1
    # os.remove(path + '/' + filename)
