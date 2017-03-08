import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
def computeMeanShift(X,q):
    # Compute clustering with MeanShift
    # The MeanShift bandwidth can be automatically detected using
    bandwidth = estimate_bandwidth(X, quantile = q, n_samples=X.shape[0])
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    print("number of estimated clusters : %d" % n_clusters_)

def plotMeanShift(X,q):
    # Compute clustering with MeanShift
    # The following bandwidth can be automatically detected using
    bandwidth = estimate_bandwidth(X, q, n_samples=X.shape[0])
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    # Plot results
    import matplotlib.pyplot as plt
    from itertools import cycle
    plt.figure(1)
    plt.clf()
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()
