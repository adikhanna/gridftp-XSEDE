import numpy as np

kdic = {}
array = []
filereadlist = []

for i in range(10):
	filereadlist.append("Channel-" + str(i) + "-inst-thr.txt")

for fname in filereadlist:
    with open(fname) as f:
    	   data = f.readlines()
    	   for d in data:
               d = d.rstrip(" ")
               d = d.split()
               kdic[int(d[0])] = int(d[1])

           for k, v in kdic.items():
	       array.append(int(v))

           stddev = np.std(array)
           fwname = "stddev.txt"
           fw = open(fwname, "a")
           fw.write("\n" + fname + "\n" + str(stddev) + "\n")

