# -*- coding: UTF-8 -*-

import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from euclideanDistance import euclideanDistance
from loadData import *

# X contient notre data 7 stats
# names contient les noms des joueurs et leur équipe
# column contient les noms des colonnes
X, names, column = loadData('data/data_players_7stats.csv')

# Plotting data
# plotData(X,column)

# Normalisation
X = (X - np.mean(X, axis = 0)) / np.std(X, axis = 0)
