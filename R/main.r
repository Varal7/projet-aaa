library(data.table)
library(TDAmapper)
library(ggplot2)
library(igraph)
library(RColorBrewer)
library(networkD3)
library(Rtsne)
library(magrittr)

# Read data
df <- read.csv("data/data_players_7stats_w_position.csv", header=TRUE)
nba.positions <- df[,8]
nba.gen_positions <- df[,9]
nba.st <- df[,1:7]

# Perform PCA
if(!exists("PCA", mode="function")) source("PCA.R")
nba.pca <- PCA(nba.st, center=FALSE, norm = TRUE)
# Compute angles
nba.angles <- atan(nba.pca$points[2,] / nba.pca$points[1,])

## Preprocess in order to apply Mapper

# Center and normalize data
nba.st <- scale(nba.st)

# Compute Variance Normalized Euclidean distance
nba.dist = dist(nba.st)

# Compute t-SNE
nba.tsne <- Rtsne(
  as.matrix(nba.st),
  check_duplicates = FALSE,
  perplexity = 100,
  theta = 0.5,
  dims = 2,
  verbose = TRUE
)

# Display Mapper graph
displayGraph <- function(res.mapper, filename) {

  # Compute graph
  nba.graph <- graph.adjacency(res.mapper$adjacency, mode="undirected")
  MapperLinks <- mapperEdges(res.mapper)
  MapperNodes <- mapperVertices(res.mapper, rownames(nba.st) )

  #Display graph
  #plot(nba.graph)

  #Display interactive graph
  #forceNetwork(Nodes = MapperNodes, Links = MapperLinks,
  #            Source = "Linksource", Target = "Linktarget",
  #            Value = "Linkvalue", NodeID = "Nodename",
  #            Group = "Nodegroup", opacity = 1,
  #            linkDistance = 10, charge = -400, zoom=TRUE)

  #name <- "Marcus Camby"
  #name <- "Tyson Chandler"
  #name <- "Bryce Cotton"
  #name <- "Stephen Curry"
  #name <- "Manu Ginobili"
  #name <- "Kevin Durant"
  #name <- "LeBron James"
  #name <- "Dirk Nowitzki"
  #name <- "LaMarcus Aldridge"
  #name <- "Kevin Love"
  name <- "Blake Griffin"
  MapperNodes["cond"]<- grepl(name,MapperNodes$Nodename)

  # Compute colors
  assoc = data.table(names = rownames(nba.st), position = as.character(nba.gen_positions))
  setkey(assoc, "names")

  nodePosition <- strsplit(as.character(MapperNodes$Nodename), ", ")
  nodeMainPosition <- c()
  for (i in 1:length(nodePosition)) {
    nodePosition[[i]][1] <- strsplit(nodePosition[[i]][1], ": ")[[1]][2]
    nodePosition[[i]] <- assoc[nodePosition[[i]]][,position]
    nodeMainPosition[i] <- names(sort(table(nodePosition[[i]]),decreasing=TRUE)[1])
  }
  MapperNodes["position"] <- nodeMainPosition

  # Display Network
  forceNetwork(Nodes = MapperNodes, Links = MapperLinks,
              Source = "Linksource", Target = "Linktarget",
              Value = "Linkvalue", NodeID = "Nodename",
              Group = "position", opacity = 1,
              colourScale = "d3.scale.category10()",
              linkDistance =
      JS('function(){d3.select("body").style("background-color", "#000000"); return 10;}'), charge = -400, zoom=TRUE) %>%

  saveNetwork(file = paste('output', filename, sep = '/'))
}

# Choose filter values

#filter_values = list(order(nba.tsne$Y[,1]), order(nba.tsne$Y[,2]))
#filter_values = list(nba.tsne$Y[,1], nba.tsne$Y[,2])
#filter_values = list(nba.pca$points[1,], nba.pca$points[2,])
filter_values = list(nba.pca$points[1,], nba.angles)
#filter_values = list(order(nba.pca$points[1,]), order(nba.angles))

# Apply Mapper
nba.mapper <- mapper(dist_object = nba.dist,
           filter_values = filter_values,
           num_intervals = c(3,3),
           percent_overlap = 50,
           num_bins_when_clustering = 5)

displayGraph(nba.mapper, "pca_angles_3.html")
