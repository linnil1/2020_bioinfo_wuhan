## 01 Sequences selection
Download from NCBI virus.

input: `sequences.csv` sequences.fasta`

output: `01_select_sequences.fasta`

```
pip install Biopython pandas matploblib numpy adjustText
python3 select_fasta.py
```

## 02 Alignmen
Input: `01_select_sequences.fasta`

Output: `02_align.aln`

```
wget https://mafft.cbrc.jp/alignment/software/mafft_7.470-1_amd64.deb
dpkg -i mafft_7.470-1_amd64.deb 
/usr/bin/mafft  --thread 16 --auto --reorder "01_select_sequences.fasta" > "02_align.fasta"
```


## 02-1 Visualization: MEGA
```
dpkg -i  megax_10.1.8-1_amd64.deb 
DEBIAN_FRONTEND=noninteractive  apt -y -f install libglu1-mesa-dev freeglut3-dev mesa-common-dev
megax
```

## 03 Sequences Trimming and pruning
Input: `02_align.fasta`

Output: `04_prune.fas` (Fasta file)

```
python3 trim_fasta.py
python3 prune_fasta.py
```


## 05 DnaSp
This is a windows GUI program.

The code is not provided.

The below code is to fix the format for downstream analysis

input: `05_haplo.nex`

Output: `05_haplo_rewrite.nex`

```
python3 rewrite.py
```

## 06 Build tree 
Init Input: `05_haplo_rewrite.nex`

Input: `06_tree.stree5`

Output: `06_tree.stree5`

```
wget https://software-ab.informatik.uni-tuebingen.de/download/splitstree5/splitstree5_unix_5_2_2-beta.sh
chmod +x splitstree5_unix_5_2_2-beta.sh
./splitstree5_unix_5_2_2-beta.sh
SplitsTree5
```

## 07 read and replot
Input: `06_tree_mst.stree5`

Output: `07_plot.png`, `07_name.csv`

```
python3 hap_to_geo.py
python3 read_replot.py "06_tree_mst.stree5" "07_plot.png"
```

## 08  Using another tree building algorithm
Input: `06_tree_mst.stree5`

Output: `08_dist.csv` `08_upgma.png` `08_upgma_circle.png`

```
python3 read_dist.py
Rscript build_tree.R 
```

## 09  Using logdet as distance
Init Input: `05_haplo_rewrite.nex`

Input: `09_tree_logdet.stree5`

Output: `09_tree_logdet.stree5` `09_plot.png`

```
SplitsTree5
python3 read_replot.py "09_tree_logdet.stree5" "09_plot.png"
```

## 10 Without haplotype
Init Input: `04_prune.fas`

Input: `10_tree_seq.stree5`

Output: `10_tree_seq.stree5` `10_plot.png`

```
SplitsTree5
python3 read_replot.py "10_tree_seq.stree5" "10_plot.png"
```