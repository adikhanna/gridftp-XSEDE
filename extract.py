# filereadlist = []

# for i in range(5):
#     filereadlist.append("stampede-comet" + str(i) + ".txt")

# for i in range(5):
#    filereadlist.append("supermic-bridges" + str(i) + ".txt")

# fwname = "time_sc.txt"

# fwname = "time_sb.txt"
# fw = open(fwname, "a")

# for fname in filereadlist:
#     with open(fname) as f:
#         for line in f:
#             if line.startswith('Time taken in seconds = '):
#                 fw.write(line.strip('Time taken in seconds = '))
#     fw.write("\n" + "Next file..." + "\n")

filereadlist = ["supermic-bridges3.txt", "stampede-comet2.txt"]
filewritelist = ["datetime_sb.txt", "datetime_sc.txt"]

j = 0

for fname in filereadlist:
    with open(fname) as f:
        fwname = filewritelist[j]
        fw = open(fwname, "a")
        for line in f:
            if line.startswith('Date & Time of transfer: '):
                fw.write(line.strip('Date & Time of transfer: '))
    j = j+1
