from Bio import SeqIO

count = 0 
seqs = []
count_sum = 0
for record in SeqIO.parse("02_align.fasta", "fasta"):
    count_sum += 1
    if record.seq[100] == '-':
        continue
    # lastone = 29906
    if record.seq[29800] == '-':
        continue
    record.seq = record.seq[100:29800]
    seqs.append(record)
    count += 1

print(count, count_sum)
# f_select_fasta = open("03_trim_sequences.fasta", "w")
# SeqIO.write(seqs, f_select_fasta, "fasta")
f_select_fasta = open("03_trim_sequences.aln", "w")
SeqIO.write(seqs, f_select_fasta, "clustal")
