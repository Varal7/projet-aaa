# -*- coding: UTF-8 -*-
# execfile('loadData.py')
from sklearn import manifold, datasets, neighbors

import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# X contient notre data 7 stats
X = np.genfromtxt('data_players_7stats.csv', delimiter = ';', skip_header = 1, usecols = range(8, 15))

def isomap(X, n_neighbors, plot = False):
    Y = manifold.Isomap(n_neighbors, 2).fit_transform(X)
    if plot:
        plt.scatter(Y[:, 0], Y[:, 1])
        plt.title('result of the ' + str(n_neighbors) + '-neighbors isomap ')
        plt.show()
    return Y

isomap(X, 3, True)
