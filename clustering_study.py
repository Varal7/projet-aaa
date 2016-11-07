# -*- coding: UTF-8 -*-
from sklearn.cluster import KMeans
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from utilitiesData import *
from pcaImp import pca


def res_kmeans(data, k = 5, plot = True, seed_tries = 10):
    kmeans = KMeans(n_clusters = k, init = 'k-means++', n_init = seed_tries).fit(data)

    if(plot):
        labels = kmeans.labels_
        (Y, perc, comp) = pca(data, 2)
        plt.scatter(Y[:, 0], Y[:, 1], c = labels)
        plt.show(block = False)

    # print('k = ', k, ', Inertia = ', kmeans.inertia_)
    return kmeans.inertia_



#
