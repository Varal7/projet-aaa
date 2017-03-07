# Inspired by Frederic Chazal and Bertrand Michel's practical lesson
# http://www.lsta.upmc.fr/michelb/Enseignements/TDA/Mapper_solutions.html

library(TDAmapper)
library(ggplot2)
library(igraph)
library(RColorBrewer)
library(networkD3)

#Read data
df <- read.csv("data/data_players_7stats_w_position.csv", header=TRUE)
nba.positions <- df[,8]
nba.gen_positions <- df[,9]
nba.st <- df[,1:7]

use_gen_positions <- TRUE

#Perform PCA
if(!exists("PCA", mode="function")) source("PCA.R")
nba.pca <- PCA(nba.st, center=FALSE, norm = TRUE)
angles <- atan(nba.pca$points[2,] / nba.pca$points[1,])


#Plot spectrum
plot(nba.pca$spectrum, type="p", ylab="S")

#Plot Variances described by each composant of the PCA
plot(nba.pca$cumulativevariance, ylab="Var", xlab="index", type="b")

#Add colors according to position
if (use_gen_positions) {
  colors<-brewer.pal(n=3,name="Set1")
  color_position<-colors[nba.gen_positions]
} else {
  colors<-brewer.pal(n=9,name="Set1")
  color_position<-colors[nba.positions]
}

#Plot PCA
plot(nba.pca$points[1,],nba.pca$points[2,], xlab="PCA1", ylab="PCA2", col=color_position)

if (use_gen_positions) {
    legend(x=0, y=6, levels(nba.gen_positions),pch=21,
           col=colors, pt.cex=2, cex=.8, bty="n", ncol=1)
} else {
    legend(x=0, y=6, levels(nba.positions),pch=21,
           col=colors, pt.cex=2, cex=.8, bty="n", ncol=1)
}

#Now apply Mapper

#Center and normalize data
nba.st <- scale(nba.st)

#Compute Variance Normalized Euclidean distance
nba.dist = dist(nba.st)

nba.mapper <- mapper(dist_object = nba.dist,
           filter_values = list(nba.pca$points[1,], angles),
           num_intervals = c(30,30),
           percent_overlap = 50,
           num_bins_when_clustering = 5)

nba.graph <- graph.adjacency(nba.mapper$adjacency, mode="undirected")

#Display graph
#plot(nba.graph)

#Display interactive graph
MapperLinks <- mapperEdges(nba.mapper)
MapperNodes <- mapperVertices(nba.mapper, rownames(nba.st) )
forceNetwork(Nodes = MapperNodes, Links = MapperLinks,
            Source = "Linksource", Target = "Linktarget",
            Value = "Linkvalue", NodeID = "Nodename",
            Group = "Nodegroup", opacity = 1,
            linkDistance = 10, charge = -400, zoom=TRUE)
