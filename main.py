# -*- coding: UTF-8 -*-
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from euclideanDistance import euclideanDistance
from loadData import *
from isomap import *
from affinityPropagation import *
from meanShift import *
from sklearn.decomposition import PCA
from pcaImp import pca
# X contient notre dataset 7 stats
# names contient les noms des joueurs et leur équipe
# column contient les noms des colonnes
X, names, column = loadData('data/data_players_7stats.csv')

# Normalisation
X = (X - np.mean(X, axis = 0)) / np.std(X, axis = 0)

# Perform PCA
# Percentage of the feature space according to eigenvalues
perc_=[]
for i in range(1,10):
	(Y,perc,comp)=pca(X,i)
	perc_.append(perc)

fig, ax1 = plt.subplots(figsize=(14,6))
plt.plot(range(1,10),perc_,'b-',label="eigen percentage")
plt.xlabel('number of components')
plt.ylabel('percentages')
plt.show()

# How to compute Mahalanobis distance
# sp.spatial.distance.mahalanobis(X[0], X[1], np.linalg.inv(np.cov(np.transpose(X))))

# Compute # de clusters selon MeanShift
# Valeur arbitrairement choisie pour aboutir à 5 clusters
quantile = 0.22
computeMeanShift(X,quantile)

# N'a pas de sens pour l'instant
# plotMeanShift(X,quantile)

# Plotting data, data distribution, boxplots
plotData(X, column)


# ploting Isomap
# isomap(X, 3, True)
