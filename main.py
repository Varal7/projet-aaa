# -*- coding: UTF-8 -*-
import math
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from utilitiesData import *
from isomap import *
# from euclideanDistance import euclideanDistance
# from affinityPropagation import *
# from meanShift import *
from clustering_study import *
from plot_kmeans_silhouette_analysis import *
from sklearn import decomposition
from pcaImp import pca
from pandas.tools.plotting import scatter_matrix
import pandas as pd
import meanShift
from sklearn.cluster import KMeans

#
#	DATA LOADING
#

# X contient notre dataset 7 stats
# names contient les noms des joueurs et leur équipe
# column contient les noms des colonnes
X, names, column = loadData('data/data_players_7stats.csv')
df = pd.DataFrame(data = X, columns = column)
#
# DATA NORMALISATION
#

# X = (X - np.mean(X, axis = 0)) / np.std(X, axis = 0)

inertias = []
for k in range(2, 40):
    clusterer = KMeans(n_clusters=k, init = 'k-means++', n_init = 10, tol = 1e-8, max_iter = 1000)
    # cluster_labels = clusterer.fit_predict(X)
    clusterer.fit(X)
    inertias.append(clusterer.inertia_)

plt.plot(inertias, 'r-')
plt.show()

# Algebrical normalization
corr = np.corrcoef(X.T)
print(np.round(corr, 2))
print(np.sum(corr, axis = 0))
X = np.dot(X, np.diag(1 / np.sum(corr, axis = 0)))

#
# DATA VISUALIZATION
#

df = pd.DataFrame(X, columns = column)
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
# plt.show()

silhouettes = []
contrasts = []

range_n_clusters = range(3, 19)
for n_clusters in range_n_clusters:
    silhouettes.append(clustering_analysis(X, singlelinkage_clustering(X, n_clusters), plot = True)[0])
    contrasts.append(clustering_analysis(X, singlelinkage_clustering(X, n_clusters))[1])

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(silhouettes, 'r-' , label = "silhouettes")
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(contrasts, 'g-', label = "contrasts")
plt.legend()
plt.show()

# plotPCA3D(X, column, names)



# clustering_analysis(X, knn_clustering(X, 5))




# Perform PCA
(Y, perc, comp) = pca(X,1)

# Plot percentage of the feature space according to eigenvalues
plotPCA(X)

# Plot Correlation Circle
plotCorrelationCircle(X, column, names)

# How to compute Mahalanobis distance
# sp.spatial.distance.mahalanobis(X[0], X[1], np.linalg.inv(np.cov(np.transpose(X))))

# Compute # de clusters selon MeanShift
# Valeur arbitrairement choisie pour aboutir à 5 clusters
quantile = 0.22
computeMeanShift(X,quantile)

# N'a pas de sens pour l'instant

plotMeanShift(X,quantile)

# Plotting data, data distribution, boxplots
# plotData(X, column)

isomap(X, 4, 1)
