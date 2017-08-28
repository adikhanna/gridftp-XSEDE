#!/usr/bin/python

import numpy as np
import glob

readfile = "average.txt"

writefile = "final.txt"
fw = open(writefile, "a")

datalist = []

with open(readfile, "r") as f:
    datalist = np.loadtxt(f)

for i in range(10):
    one = datalist[i]
    two = datalist[i+10]
    three = datalist[i+20]
    four = datalist[i+30]
    five = datalist[i+40]

    sum = int(one)+int(two)+int(three)+int(four)+int(five)
    avg = sum/5

    fw.write("Channel_" + str(i) + " Average:" + "\n" + str(avg) + "\n")
