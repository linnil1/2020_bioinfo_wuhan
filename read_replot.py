import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from adjustText import adjust_text
import numpy as np
import sys


# read tree
start = False
node = [""] * 200
pos = [[]] * 200
edge = []
maxid = 0

if len(sys.argv) < 3:
    print("python3 read_replot.py xx.stree5 xx.png")
    sys.exit()
file_in = sys.argv[1]
file_out = sys.argv[2]

for line in open(file_in):
    if start:
        if "N: " in line:
            s = re.findall(r"N: (\d+) (.*)f S", line)[0]
            id = int(s[0])
            p = np.array(s[1].split(), dtype=np.float)
            text = re.findall(r"L: '(\w+)", line)
            node[id] = text[0] if text else ""
            pos[id] = p
            maxid = max(maxid, id)

        if "E: " in line:
            ids = re.findall(r"E: (\d+) (\d+)", line)[0]
            id1, id2 = int(ids[0]), int(ids[1])
            s = re.findall(r"'(.*)'", line)[0]
            s = s.replace("L", "").replace("M", "")
            edge.append((id1, id2))

        if line.startswith("END"):
            break

    if line.startswith("LINK ALGORITHM = NetworkEmbedder"):
        start = True


name_table = pd.read_csv("07_name.csv")
print(name_table)

node = node[1:maxid+1]
pos = np.stack(pos[1 : maxid+1])
edge = np.array(edge[1 : maxid+1]) - 1
print(node)
print(pos)
print(edge)

# cont_color = dict(zip(sorted(set(name_table["continent"])), list(mcolors.TABLEAU_COLORS.values())))
cont_color = {'Asia':    '#1f77b4',
              'Africa':  '#d62728',
              'Europe':  '#ff7f0e',
              'America': '#9467bd',
              'Oceania': '#2ca02c'}
print(cont_color)

plt.figure(num=None, figsize=(16, 9), dpi=100, facecolor='w', edgecolor='k')
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
plt.plot(pos[:, 0], pos[:, 1], '.')
for i in edge:
    plt.plot(pos[i, 0], pos[i, 1], 'black', '-')

texts = []
for i in range(maxid):
    if node[i].startswith("Hap"):
        subt = name_table[name_table["hap"] == node[i]] 
    else:
        subt = name_table[name_table["accession"] == node[i]] 
    if not len(subt):
        continue
    for j in range(len(subt)):
        texts.append(plt.text(pos[i, 0], pos[i, 1], subt.iloc[j]['short'], color=cont_color[subt.iloc[j]['continent']]))

adjust_text(texts, precision=.5)
plt.legend(handles=[mpatches.Patch(color=c, label=name) for (name, c) in cont_color.items()])
plt.savefig(file_out)
plt.show()
