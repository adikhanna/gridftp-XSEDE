#!/usr/bin/python

import numpy as np
import glob

filereadlist = []
writefile = "average.txt"
f = open(writefile, "a")

for j in [1]:
    for i in range(5):
        path = "/Users/administrator/Downloads/AllFigures_LargeDataset/Frequency_" + str(j) + "/Trial_" + str(i+1) + "/stddev_" + str(j) + "_" + str(i+1) + ".txt"
        filereadlist.append(path)

for fname in filereadlist:
    #f.write(fname)
    file = open(fname, "r")
    for line in file:
        if line.startswith('Channel'):
            continue
        else:
            line.strip(" ")
            f.write(line + "\n")
