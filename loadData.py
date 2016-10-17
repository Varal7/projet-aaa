# -*- coding: UTF-8 -*-

import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# X contient notre data 7 stats
X = np.genfromtxt('data_players_7stats.csv', delimiter = ';', skip_header = 1, usecols = range(8, 15))
# names contient les noms des joueurs et leur équipe
names = np.genfromtxt('data_players_7stats.csv', delimiter = ';', skip_header = 1, usecols = range(1, 3), dtype = str)
# column contient les noms des colonnes
with open('data_players_7stats.csv', 'r') as f:
    first_line = f.readline()

column = first_line.strip().split(';')
for index in range(0, 8):
    column.pop(0)

print(column)

# plot distribution over features
fig = plt.figure("Data distribution")
for index in range(0, len(X[0])):
    plt.subplot(3, 3, 1 + index)
    plt.hist(X[:, index], 50)
    plt.xlabel(column[index])
    plt.ylabel('Effectif')

plt.suptitle('Data distribution')
# fig.savefig('Data distribution.png')
plt.show(block = False)

fig = plt.figure("Data vizualisation")
for index in range(0, len(X[0])):
    plt.subplot(3, 3, 1 + index)
    plt.plot(range(0, 476), X[:, index], 'ro')
    plt.ylabel(column[index])
    plt.xlabel('player_id')

plt.suptitle('Data vizualisation')
# fig.savefig('Data vizualisation.png')

plt.show(block = False)

# au cas où on veut corriger, utiliser where pour récupérer les indices
# odd = np.where(X[:,6] > 10)[0]
