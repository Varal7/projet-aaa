library(data.table)
library(TDAmapper)
library(ggplot2)
library(igraph)
library(RColorBrewer)
library(networkD3)
library(Rtsne)
library(magrittr)

# Read data
df <- read.csv("../data/data_players_7stats_w_position.csv", header=TRUE)
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

# Display Mapper graph
saveGraphColorPlayers <- function(res.mapper, orig_name, players) {

  # Compute graph
  nba.graph <- graph.adjacency(res.mapper$adjacency, mode="undirected")
  MapperLinks <- mapperEdges(res.mapper)
  MapperNodes <- mapperVertices(res.mapper, rownames(nba.st) )

  for (iPos in 1:length(allPlayers)) {
   players<-allPlayers[[iPos]]

    # Compute color for names
    nodePlayers <- strsplit(as.character(MapperNodes$Nodename), ", ")
    nodePlayersToColor <- c()
    for (i in 1:length(nodePlayers)) {
      nodePlayers[[i]][1] <- strsplit(nodePlayers[[i]][1], ": ")[[1]][2]
      notFound <- TRUE
      for (j in 1:length(players)) {
        if (players[j] %in% nodePlayers[[i]]) {
          nodePlayersToColor[i] <- players[j]
          notFound <- FALSE
        }
      }
      if (notFound) {
          nodePlayersToColor[i] <- "Other"
      }
    }
    MapperNodes["players"] <- nodePlayersToColor

    # Display Network (Black)
    filename <- paste("player", iPos, orig_name, "black" , sep="_")
    forceNetwork(Nodes = MapperNodes, Links = MapperLinks,
                Source = "Linksource", Target = "Linktarget",
                Value = "Linkvalue", NodeID = "Nodename",
                Group = "players", opacity = 1,
                colourScale = "d3.scale.category10()",
                legend = TRUE,
                linkDistance =
        JS('function(){d3.select("body").style("background-color", "#000000"); d3.select("body").style("fill", "#ffffff"); return 10;}'), charge = -400, zoom=TRUE) %>%
    saveNetwork(file = paste(filename, "html", sep="."))

    # Display Network (White)
    filename <- paste("player", iPos, orig_name, "white" , sep="_")
    forceNetwork(Nodes = MapperNodes, Links = MapperLinks,
                Source = "Linksource", Target = "Linktarget",
                Value = "Linkvalue", NodeID = "Nodename",
                Group = "players", opacity = 1,
                colourScale = "d3.scale.category10()",
                legend = TRUE,
                linkDistance =
        JS('function(){d3.select("body").style("background-color", "#ffffff"); d3.select("body").style("fill", "#000000"); return 10;}'), charge = -400, zoom=TRUE) %>%
    saveNetwork(file = paste(filename, "html", sep="."))
  }
}

# List possible filters

filters = list(
    list(nba.pca$points[1,], nba.pca$points[2,]),
    list(nba.pca$points[1,], nba.angles),
    # list(nba.tsne$Y[,1], nba.tsne$Y[,2]),
    list(order(nba.pca$points[1,]), order(nba.pca$points[2,])),
    # list(order(nba.tsne$Y[,1]), order(nba.tsne$Y[,2])),
    list(order(nba.pca$points[1,]), order(nba.angles))
)

# Choose parameters

filter_value_id = 1
num_intervals_x = 30
num_intervals_y = 30
percent_overlap = 50
num_bins = 25
num_intervals <- 30

# filter_value_id = 1
# num_intervals_x = 5
# num_intervals_y = 5
# percent_overlap = 50
# num_bins = 5
# num_intervals <- 5
# Apply Mapper

allPlayers <- list(
  c("Jason Terry", "Tony Parker"),
  c("Mike Conley", "Kyle Lowry"),
  c("Jameer Nelson", "John Wall"),
  c("Stephen Curry", "Manu Ginobili"),
  c("Arron Afflalo", "Rudy Fernandez"),
  c("Luol Deng", "Chase Budinger"),
  c("Dirk Nowitzki", "LaMarcus Aldridge"),
  c("Marcus Camby", "Tyson Chandler"),
  c("Kevin Love", "Blake Griffin"),
  c("Shane Battier", "Ronnie Brewer"),
  c("Kevin Durant", "LeBron James"),
  c("Rudy Gay", "Caron Butler"),
  c("Derrick Rose", "Dwight Howard")
)

# for (filter_value_id in c(1,2,3,4,5,6)) {
 for (filter_value_id in c(1,2)) {
   for (num_bins in c(5, 10, 15, 20, 25)) {
#     for (percent_overlap in c (40, 50, 60)) {
#       for (num_intervals in c(10, 20, 30, 40)) {


 # for (filter_value_id in c(1)) {
  #  for (num_bins in c(20)) {

          num_intervals_x <- num_intervals
          num_intervals_y <- num_intervals

          name <- paste(filter_value_id, num_intervals_x, num_intervals_y, percent_overlap, num_bins, sep="_")
          print(name)
          tic <- proc.time()
          nba.mapper <- mapper(dist_object = nba.dist, filter_values = filters[filter_value_id], num_intervals = c(num_intervals_x,num_intervals_y), percent_overlap = percent_overlap, num_bins_when_clustering = num_bins)
          tac <- proc.time()
          print(tac - tic)
          saveGraphColorPlayers(nba.mapper, paste(name, sep="_"), allPlayers)
    }
  }
