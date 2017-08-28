#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

filelist = []
datalist = []

for i in range(10):
    filelist.append("Channel-" + str(i) + "-inst-thr.txt")

fig = plt.figure()
plt.rcParams.update({'font.size': 6})
plt.title('Frequency = 1s : Trial 3', fontsize =12, y=1.03)
plt.xlabel('Epoch Time', fontsize = 12, labelpad = 18)
plt.ylabel('Instantaneous Throughput', fontsize = 12, labelpad = 20)

for fname in filelist:
    data = np.loadtxt(fname)
    datalist.append(data)

for i in range(10):
    X = datalist[i][:, 0]
    Y = datalist[i][:, 1]
    name = "Channel " + str(i)
    ax = fig.add_subplot(5,2,i+1)
    ax.plot(X, Y, 'ro', markersize=2, linestyle='solid')
    ax.set_title(name)
    xticks = ticker.MaxNLocator(10)
    ax.xaxis.set_major_locator(xticks)

plt.tight_layout()
plt.subplots_adjust(hspace = 0.6)
plt.savefig("Frequency_1: Trial_3.png", dpi=600)
