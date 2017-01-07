# Inspired by Frederic Chazal and Bertrand Michel's practical lesson
# http://www.lsta.upmc.fr/michelb/Enseignements/TDA/Mapper_solutions.html

library(TDAmapper)
library(ggplot2)
library(igraph)

#Compute a data and plot it
First.Example.data = data.frame( x=2*cos(0.5*(1:100)), y=sin(1:100) )
qplot(First.Example.data$x,First.Example.data$y)

#Use euclidean distance
First.Example.dist = dist(First.Example.data)

#Apply Mapper
First.Example.mapper <- mapper(dist_object = First.Example.dist,
           filter_values = First.Example.data$x,
           num_intervals = 6,
           percent_overlap = 50,
           num_bins_when_clustering = 10)

First.Example.graph <- graph.adjacency(First.Example.mapper$adjacency, mode="undirected")


#Compute the size of each vertex
vertex.size <- rep(0,First.Example.mapper$num_vertices)
for (i in 1:First.Example.mapper$num_vertices){
  points.in.vertex <- First.Example.mapper$points_in_vertex[[i]]
  vertex.size[i] <- length((First.Example.mapper$points_in_vertex[[i]]))
}
V(First.Example.graph)$size <- vertex.size

plot(First.Example.graph, layout = layout.auto(First.Example.graph) )


#Alternatively, display an interactive plot

library(networkD3)
MapperNodes <- mapperVertices(First.Example.mapper, 1:100 )
MapperLinks <- mapperEdges(First.Example.mapper)

forceNetwork(Nodes = MapperNodes, Links = MapperLinks,
            Source = "Linksource", Target = "Linktarget",
            Value = "Linkvalue", NodeID = "Nodename",
            Group = "Nodegroup", opacity = 1,
            linkDistance = 10, charge = -400)
