import re
import numpy as np
import pandas as pd

start = False
ids = []
dist = []

for line in open("06_tree_mst.stree5"):
    if start:
        s = re.findall(r"\[\d+\]\s*'(\w+)'\s*(.*)$", line)
        if not s:
            continue
        ids.append(s[0][0])
        dist.append(s[0][1].split())

        if line.startswith("END"):
            break

    if line == "LINK ALGORITHM = Uncorrected_P;\n":
        start = True


print(ids)
df = pd.DataFrame(np.array(dist, dtype=np.float), index=ids, columns=ids)
df.to_csv("08_dist.csv")

