from numpy import *

#data : the data matrix
#k the number of component to return
#return the new data and  the variance that was maintained AND the principal components (ALL)
def pca(data,k):
    # Performs principal components analysis (PCA) on the n-by-p data matrix A (data)
    # Rows of A correspond to observations (wines), columns to variables.
    ## TODO: Implement PCA

    M = mean(data,0) # compute the mean
    C = data - M # subtract the mean (along columns)
    W = dot(transpose(C),C) # compute covariance matrix
    eigval,eigvec = linalg.eig(W) # compute eigenvalues and eigenvectors of covariance matrix
    idx = eigval.argsort()[::-1] # Sort eigenvalues
    eigvec = -eigvec[:,idx] # Sort eigenvectors according to eigenvalues
    # Project the data to the new space (k-D)
    return (dot(C,real(eigvec[:,:k])),sum(eigval[:k]) /sum(eigval[:]), eigvec)
