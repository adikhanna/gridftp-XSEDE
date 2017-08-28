#!/usr/bin/python
import numpy as np

filelist = []
totalsum = 0

fw = open("writefile.txt", "r+")

for i in range(10):
    filelist.append("Channel-" + str(i) + "-inst-thr.txt")

for fname in filelist:
    mysum = 0
    with open(fname,'r') as f:
        for line in f:
            mysum += int(line.split()[1])
    fw.write(str(mysum) + "\n")
    totalsum = totalsum + mysum

fw.write(str(totalsum) + "\n")

fw.close()
