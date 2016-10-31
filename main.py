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

# X contient notre dataset 7 stats
# names contient les noms des joueurs et leur équipe
# column contient les noms des colonnes
X, names, column = loadData('data/data_players_7stats.csv')


# Compute Mahalanobis distance
sp.spatial.distance.mahalanobis(X[0], X[1], np.linalg.inv(np.cov(np.transpose(X))))

# Compute # de clusters selon MeanShift
computeMeanShift(X)

# N'a pas de sens pour l'instant
# plotMeanShift(X)

# Plotting data and data distribution
# plotData(X, column)

# Normalisation
# X = (X - np.mean(X, axis = 0)) / np.std(X, axis = 0)

# ploting Isomap
# isomap(X, 3, True)
