# -*- coding: UTF-8 -*-

import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def loadData(s):
    X = np.genfromtxt(s, delimiter = ';', skip_header = 1, usecols = range(8, 15))
    # names contient les noms des joueurs et leur équipe
    names = np.genfromtxt(s, delimiter = ';', skip_header = 1, usecols = range(1, 3), dtype = str)
    # column contient les noms des colonnes
    with open(s, 'r') as f:
        first_line = f.readline()
    column = first_line.strip().split(';')
    for index in range(0, 8):
        column.pop(0)
    return X, names, column


def plotData(X, column):
    # plot distribution over features
    fig = plt.figure("Data distribution")
    plt.suptitle('Data distribution')
    for index in range(0, len(X[0])):
        plt.subplot(3, 3, 1 + index)
        plt.hist(X[:, index], 50)
        plt.xlabel(column[index])
        plt.ylabel('Effectif')
    fig = plt.figure("Data vizualisation")
    plt.suptitle('Data vizualisation')
    for index in range(0, len(X[0])):
        plt.subplot(3, 3, 1 + index)
        plt.plot(range(0, 476), X[:, index], 'ro')
        plt.ylabel(column[index])
        plt.xlabel('player_id')
    plt.show()
