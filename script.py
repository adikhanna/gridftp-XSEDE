import subprocess

#for i in [1,3,5,10]:
#    for j in range (10):
#        command = "mkdir freq_" + str(i) + "/" + "channel_" + str(j)
#        process = subprocess.Popen([command], shell = True)

# for i in [1,3,5,10]:
#     for j in range(5):
#         for k in range(10):
#             basecommand = "mv throughput_" + str(i) + "_" + str(j) + "/Channel-" + str(k) + "-inst-thr.txt"
#             command = basecommand + " freq_" + str(i) + "/channel_" + str(k)
#             process = subprocess.Popen([command], shell=True)

for i in [1, 3, 5, 10]:
    for j in range(5):
        path = "/home/avkhann2/Desktop/Project_Data/HARP_Data/samplingdata_large/channel-throughput/freq_" + str(i) + "/"
        full_path = path + str(j)
        #command = "cp " + full_path + "/writefile.txt " + full_path + "/writefile.rtf"
        #next_command = "rm " + full_path + "/writefile.txt"
        other_command = "cp " + full_path + "/stddev_" + str(i) + "_" + str(j+1) + ".txt" + " " + full_path + "/stddev_" + str(i) + "_" + str(j+1) + ".rtf"
        again_command = "rm " + full_path + "/stddev_" + str(i) + "_" + str(j+1) + ".txt"
        #process = subprocess.Popen([command], shell=True)
        #process1 = subprocess.Popen([next_command], shell=True)
        process2 = subprocess.Popen([other_command], shell=True)
        process3 = subprocess.Popen([again_command], shell=True)

