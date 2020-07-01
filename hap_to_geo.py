import pandas as pd
from datetime import datetime
import re
from pprint import pprint
import country_converter as coco


# Map id to geo
data = pd.read_csv("sequences.csv")
map_acc_geo = {}
for i in range(2, len(data)):
    # dat = datetime.strptime(data.loc[i, "Collection_Date"], "%Y-%m-%d")  
    geo = data.loc[i, "Geo_Location"].split(':')[0]
    id = data.loc[i, "Accession"].split(':')[0]
    map_acc_geo[id] = geo
# print(map_acc_geo)

# Map hap to id
map_hap_acc = {}
start = 0
for line in open("05_haplo_rewrite.nex"):
    if start > 1:
        if not line.strip():
            break
        # [Hap_1:  2    MN938384 MN997409]
        a = re.findall(r"(\w+)", line)
        map_hap_acc[a[0]] = a[2:]
    if line.strip() == "[Hap#  Freq. Sequences]":
        start += 1
# print(map_hap_acc)

# Map hap to geo
map_hap_geo = {}
for (hap, acc) in map_hap_acc.items():
    map_hap_geo[hap] = [map_acc_geo[i] for i in acc]

# map country to it's region
df = []
for hap, country in map_hap_geo.items():
    for i, geo in enumerate(country):
        df.append({
            'hap': hap,
            'country': geo,
            'accession': map_hap_acc[hap][i],
            'continent': coco.convert(names=geo, to='Continent'),
            'short': coco.convert(names=geo, to='ISO3')
        })


df = pd.DataFrame(df)
print(df)
df.to_csv("07_name.csv", index=False)
