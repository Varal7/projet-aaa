# -*- coding: UTF-8 -*-
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from utilitiesData import *
from isomap import *
# from euclideanDistance import euclideanDistance
# from affinityPropagation import *
# from meanShift import *
from clustering_study import *
from plot_kmeans_silhouette_analysis import *
from sklearn import decomposition
# from pcaImp import pca

#
#	DATA LOADING
#

# X contient notre dataset 7 stats
# names contient les noms des joueurs et leur équipe
# column contient les noms des colonnes
X, names, column = loadData('data/data_players_7stats.csv')

#
# DATA NORMALISATION
#

X = (X - np.mean(X, axis = 0)) / np.std(X, axis = 0)

# inertias = []
# for k in range(2, 40):
#     inertias.append(res_kmeans(X, k = k, plot = False, seed_tries = 10))
#     print(k)
#
# plt.plot((inertias), 'r-')
# plt.show()

silhouettes = []
range_n_clusters = range(3, 19)
for n_clusters in range_n_clusters:
    silhouettes.append(clustering_analysis(X, n_clusters))

plt.figure()
plt.plot(silhouettes, 'r-')
plt.show()



# Perform PCA
(Y, perc, comp) = pca(X,1)

# Plot percentage of the feature space according to eigenvalues
# plotPCA(X)

# Plot Correlation Circle
# plotCorrelationCircle(X, column, names)

# How to compute Mahalanobis distance
# sp.spatial.distance.mahalanobis(X[0], X[1], np.linalg.inv(np.cov(np.transpose(X))))

# Compute # de clusters selon MeanShift
# Valeur arbitrairement choisie pour aboutir à 5 clusters
# quantile = 0.22
# computeMeanShift(X,quantile)

# N'a pas de sens pour l'instant
# plotMeanShift(X,quantile)

# Plotting data, data distribution, boxplots
# plotData(X, column)
