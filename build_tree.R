# install
if (!requireNamespace("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
if (!require("ggtree"))
    BiocManager::install("ggtree")
if (!require("phangorn"))
    install.packages("phangorn")
if (!require("ggplot2"))
    install.packages("ggplot2")

# import library
library("ggtree")
library("phangorn")
library("ggplot2")

# read distances
setwd("/app")
mydist = read.csv("08_dist.csv", header=TRUE, row.names = 1)
mydist = mydist[, -which(names(mydist) %in% c("Hap_133"))]
mydist = mydist[-which(rownames(mydist) %in% c("Hap_133")),]

# read metadata
mymeta = read.csv("07_name.csv", header=TRUE)
hap_to_name = mymeta[!duplicated(mymeta[,c('hap')]),]
hap_to_name = hap_to_name[-which(hap_to_name$hap %in% c("Hap_133")),]
rownames(hap_to_name) <- hap_to_name$hap

# bulid tree
dist_tree <- upgma(mydist)

# upgma
png(filename="08_upgma.png", width = 1000, height = 1500, unit = "px")
ggtree(dist_tree) %<+% hap_to_name +
geom_tiplab(aes(label=country, color=continent), size=3) +
scale_color_manual(values=c('#d62728', '#9467bd', '#1f77b4', '#ff7f0e', '#2ca02c')) +
geom_treescale()
dev.off()


# circlular plot
png(filename="08_upgma_circle.png")
ggtree(dist_tree, branch.length='none', layout='circular') %<+% hap_to_name +
geom_tiplab(aes(label=country, color=continent), size=3) +
scale_color_manual(values=c('#d62728', '#9467bd', '#1f77b4', '#ff7f0e', '#2ca02c'))
dev.off()
