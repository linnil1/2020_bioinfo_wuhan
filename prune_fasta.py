from Bio import SeqIO, Seq
import re

records = []

for record in SeqIO.parse("03_trim_sequences.fasta", "fasta"):    
    q = re.sub(r"[^atcgn\-\.]", r"n", str(record.seq))  
    for i in range(len(record)):
        if record.seq[i] != q[i]:
            print(record.seq[i])
    record.seq = Seq.Seq(q)
    records.append(record)

f_select_fasta = open("04_prune.fas", "w")
SeqIO.write(records, f_select_fasta, "fasta")     
