from Bio import SeqIO
import pandas as pd
from datetime import datetime

data = pd.read_csv("sequences.csv")
accid = []
country = set([i.split(':')[0] for i in set(data["Geo_Location"])])
country_count = {c: 0 for c in country}


for i in range(2, len(data)):
    try:
        dat = datetime.strptime(data.loc[i, "Collection_Date"], "%Y-%m-%d")  
        c = data.loc[i, "Geo_Location"].split(':')[0]
    except ValueError:
        continue
    if dat <= datetime(2020, 4, 15) and country_count[c] < 10:
        accid.append(data.loc[i, "Accession"])
        country_count[c] += 1
        print(dat)


count = 0 
seqs = []
for record in SeqIO.parse("sequences.fasta", "fasta"):
    if record.id.split('.')[0] in accid:
        record.id = record.id.split('.')[0]
        count += 1
        seqs.append(record)

print(count)
f_select_fasta = open("01_select_sequences.fasta", "w")
SeqIO.write(seqs, f_select_fasta, "fasta")
