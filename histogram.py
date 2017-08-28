import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

names = ('Channel 0', 'Channel 1', 'Channel 2', 'Channel 3', 'Channel 4', 'Channel 5', 'Channel 6', 'Channel 7', 'Channel 8', 'Channel 9')
y_pos = np.arange(len(names))

with open("writefile.txt",'r') as f:
    head = list(islice(f, 10))

plt.bar(range(len(head)), head, align='center', alpha=0.5)
plt.xticks(y_pos, names, fontsize=7)
plt.ylabel('Data transferred in bytes', labelpad = 12)
plt.title('Data Transferred by Each Channel: Trial 3')
plt.grid(True)

plt.tight_layout()
plt.savefig("DataTransferred_1_3.png", dpi=600)
