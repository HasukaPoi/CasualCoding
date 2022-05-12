import os
import sys
import re
from PIL import Image
from shutil import copy
from datetime import datetime


def pickImage(path: str, ratio1, ratio2=0):
    # make ratio
    ratio1 = parse_ratio(ratio1)
    if ratio2 == 0:
        ratio2 = ratio1*1.1
        ratio1 = ratio1*0.9
    else:
        ratio2 = parse_ratio(ratio2)

    if ratio1 > ratio2:
        ratio1, ratio2 = ratio2, ratio1

    # check input path
    if not os.path.exists(path):
        print("{} not exists.".format(path))
        return

    # mkdir outputpath
    outputpath = os.path.join(path, "{:.2f}_{:.2f}".format(ratio1, ratio2))
    if os.path.exists(outputpath):
        outputpath = os.path.join(path, "{:.2f}_{:.2f}_{}".format(
            ratio1, ratio2, datetime.now().strftime("%Y%m%d%H%M%S")))
    os.mkdir(outputpath)

    # main process
    for root, dirs, files in os.walk(path, topdown=True):
        files_filtered = list(
            filter(lambda x: x.endswith((".jpg", ".jpeg", ".png")), files))
        for f in files_filtered:
            fullpath = os.path.join(path, f)
            im = Image.open(fullpath)
            ratio = im.width/im.height
            if ratio1 <= ratio <= ratio2:
                copy(fullpath, outputpath)


def parse_ratio(r: str):
    try:
        if not re.match(r'^[0-9]+/[0-9]+$', r) == None:
            strlist = str.split(r, "/")
            ratio = float(strlist[0])/float(strlist[1])
        else:
            ratio = float(r)
    except (ValueError, ZeroDivisionError):
        print("The input {} is not effective as ratio.".format(r))
        return 0

    if ratio <= 0:
        print("The input {} is not effective as ratio.".format(r))
        return 0
    else:
        return ratio


if __name__ == '__main__':
    if len(sys.argv) == 3:
        pickImage(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 3:
        pickImage(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Check Input")
