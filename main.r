# Inspired by Frederic Chazal and Bertrand Michel's practical lesson
# http://www.lsta.upmc.fr/michelb/Enseignements/TDA/Mapper_solutions.html

library(TDAmapper)
library(ggplot2)
library(igraph
library(RColorBrewer)

#Read data
df <- read.csv("data/data_players_7stats_w_position.csv", header=TRUE)
nba.positions <- df[,9]
nba.gen_positions <- df[,10]
nba.names <- df[,1]
nba.st <- df[,2:8]

use_gen_positions <- FALSE

#Perform PCA
if(!exists("PCA", mode="function")) source("PCA.R")
nba.pca <- PCA(nba.st, norm = TRUE)

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
#Eventaully showing names
#text(nba.pca$points[1,],nba.pca$points[2,],labels=df[,1], pos =3 )
