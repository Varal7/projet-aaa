# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from sklearn import manifold, datasets, neighbors

def isomap(X, n_neighbors, plot = False):
    Y = manifold.Isomap(n_neighbors, 2).fit_transform(X)
    if plot:
        plt.scatter(Y[:, 0], Y[:, 1])
        plt.title('result of the ' + str(n_neighbors) + '-neighbors isomap ')
        plt.show()
    return Y
