# -*- coding: UTF-8 -*-

import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from pcaImp import pca
from functools import partial


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
    plt.figure('Boxplot')
    plt.suptitle('Boxplot')
    plt.boxplot(X)
    plt.xticks([1,2,3,4,5,6,7],column)
    plt.show()

def plotPCA(X):
    perc_=[]
    for i in range(1,10):
    	(Y,perc,comp)=pca(X,i)
    	perc_.append(perc)

    fig, ax1 = plt.subplots(figsize=(14,6))
    plt.plot(range(1,10),perc_,'b-',label="eigen percentage pca maison")
    plt.legend()
    plt.xlabel('number of components')
    plt.ylabel('percentages')
    plt.show()

def plotCorrelationCircle(X, column):
    (Y, perc, comp) = pca(X,2)
    print("variance : " + str(perc))
    # Calculate how important each feature was
    scr = np.dot(np.linalg.inv(np.diag(np.std(X, axis=0))),comp)
    # Scale results to match when we plot them
    scr = scr/np.linalg.norm(scr, axis=0)
    #scatter plot on principal components
    ##we need this function only to update the scatter plot when we select points
    def onpick(event, axes, Y):
    	ind = event.ind
    	axes.annotate(names[ind], (Y[ind, 0], Y[ind, 1]))
    	plt.draw()
    fig, ax1 = plt.subplots(figsize=(14, 6))
    ax1.scatter(Y[:, 0], Y[:, 1],picker = True)
    fig.canvas.mpl_connect('pick_event', partial(onpick, axes = ax1, Y = Y))
    for i,v in enumerate(column):
    	ax1.plot([0, scr[i,0]], [0, scr[i,1]], 'r-', linewidth=2,)
    	plt.text(scr[i,0]* 1.15, scr[i,1] * 1.15, v, color='r', ha='center', va='center')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.xaxis.grid(True)
    ax1.yaxis.grid(True)
    plt.xlabel('1st Principal Component')
    plt.ylabel('2nd Principal Component')
    plt.show()
