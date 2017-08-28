import numpy as np
import matplotlib.pyplot as plt
import glob
import os

filelist = []

for i in range(5):
    path = '/home/avkhann2/Desktop/Project_Data/HARP_Data/samplingdata_large/channel-throughput/freq_1/' + str(i)
    for filename in glob.glob(os.path.join(path, '*.txt')):
        filelist.append(filename)

filelist.sort()

# filereadlist = []
#
# for j in range(5):
#     for i in range(10):
# 	       filereadlist.append(str(j) + "\Channel-" + str(i) + "-inst-thr.txt")

datalist = []
color_array = ['#000000', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#008000', '#800080', '#C0C0C0'];

plt.figure()
plt.rcParams.update({'font.size': 6})
plt.title('Frequency = 1s : All Trials', fontsize =12, y=1.03)
plt.xlabel('Epoch Time', fontsize = 12, labelpad = 18)
plt.ylabel('Instantaneous Throughput', fontsize = 12, labelpad = 20)
plt.grid(True)

for fname in filelist:
    data = np.loadtxt(fname)
    datalist.append(data)

xmin = datalist[0][0][0]
xmax = datalist[49][0][0]

for i in range(10):
    X = datalist[i][:, 0]
    Y = datalist[i][:, 1]
    c = color_array[i]
    l = 'Channel ' + str(i)
    plt.legend(loc='best', prop={'size':4.2})
    plt.plot(X, Y, linestyle='solid', color=c, marker='o', markersize='2', label=l) #linewidth, mew

for j in range(10, 50):
    X = datalist[j][:, 0]
    Y = datalist[j][:, 1]
    c = color_array[j%10]
    plt.plot(X, Y, linestyle='solid', color=c, marker='o', markersize='2') #linewidth, mew

plt.xlim([xmin, xmax])

plt.tight_layout()
plt.subplots_adjust(hspace = 0.6)
plt.savefig("Frequency_1: All_Trials_Plot.png", dpi=600)
