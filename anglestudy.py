import numpy as np
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
from xgboost import plot_tree
from sklearn import decomposition
from tqdm import *

from utilitiesData import *
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

def fengineering(X):
    # X = (X - np.mean(X, axis = 0)) / np.std(X, axis = 0)
    # tan()
    # pca = PCA(n_components = 1)
    # first_component = pca.fit_transform(X)
    # X.append()
    return X


def error_predict_origin(X0 = np.array([0, 0])):
    X = pd.read_csv('data/data_2010-2011.csv', sep = ',')
    df = pd.DataFrame(data = X)

    d = dict(zip(df['GenPosition'].unique(), range(df['GenPosition'].unique().size)))
    df['GenPosition'] = df['GenPosition'].apply(lambda x:d[x])

    predictors = ['Rebounds', 'Assists', 'Turnovers', 'Steals', 'Blocks', 'PersonalFouls', 'Points']

    df[predictors] = df[predictors] / np.std(df[predictors], axis = 0)

    pca = decomposition.PCA(2)
    pca.fit(df[predictors])
    projection = np.dot(df[predictors], pca.components_.T)
    projection -= X0
    angle = np.zeros((projection.shape[0], 1))
    angle[projection[:, 0] == 0, 0] = np.pi / 2
    angle[projection[:, 0] != 0, 0] = np.arctan(projection[projection[:, 0] != 0][:, 1] / projection[projection[:, 0] != 0][:, 0])


    score = score_prediction(angle, df['GenPosition'])
    return score


def score_prediction(X, Y):
    clf = xgb.XGBClassifier(n_estimators = 10,
                                max_depth = 5,
                                objective = 'multi:softmax',
                                subsample = 0.5)
    clf.fit(X, Y, eval_set = [(X, Y)], verbose = False)

    evals_result = clf.evals_result()

    score = evals_result["validation_0"]["merror"][-1]
    return score


def optimize_origin(grid, xmin, xmax, ymin, ymax):
    scores = np.zeros([grid, grid])
    for i in tqdm(range(grid)):
        for j in tqdm(range(grid)):
            origin = np.array([xmin + (xmax - xmin) * i / grid, ymax + (ymin - ymax) * j / grid])
            scores[i, j] = error_predict_origin(origin)

    print(scores)
    plt.imshow(scores, cmap='hot', interpolation='nearest')
    plt.show()

    # return scores


def main():
    optimize_origin(50, -20, 20, -20, 20)

if  __name__ =='__main__':main()

    #
