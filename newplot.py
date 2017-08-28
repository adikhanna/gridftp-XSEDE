#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

filelist = []
datalist = []
color_array = ['#000000', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#008000', '#800080', '#C0C0C0'];

for i in range(10):
    filelist.append("Channel-" + str(i) + "-inst-thr.txt")

plt.figure()
plt.rcParams.update({'font.size': 6})
plt.title('Frequency = 1s : Trial 3', fontsize =12, y=1.03)
plt.xlabel('Epoch Time', fontsize = 12, labelpad = 18)
plt.ylabel('Instantaneous Throughput', fontsize = 12, labelpad = 20)
plt.grid(True)

for fname in filelist:
    data = np.loadtxt(fname)
    datalist.append(data)

for i in range(10):
    X = datalist[i][:, 0]
    Y = datalist[i][:, 1]
    c = color_array[i]
    l = 'Channel ' + str(i)
    plt.plot(X, Y, linestyle='solid', color=c, marker='o', markersize='2', label=l) #linewidth, mew
    plt.legend(loc='best', prop={'size':4.2})

plt.tight_layout()
plt.subplots_adjust(hspace = 0.6)
plt.savefig("Frequency_1: Trial_3_Plot.png", dpi=600)
