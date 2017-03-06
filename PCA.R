### INF563 (2015-2016)
### Copyright (C) 2015 by M. Carrière and S. Oudot

PCA <- function(cloud, center = TRUE, norm=FALSE){ # cloud: data frame, norm: boolean (true if data must be normalized)

# number of data points (= number of lines)
np <- length(cloud[[1]])

# convert data frame to numeric matrix
m <- data.matrix(cloud)

# center (and normalize) data
#m <- scale(m, center = center, norm = norm)

# compute covariance matrix
cov <- (t(m) %*% m)/np

# diagonalize covariance matrix
eig <- eigen(cov)

# retrieve eignvectors and eigenvalues
vec <- eig$vectors
vars <- eig$values

# compute new coordinates
reduced <- t(vec) %*% t(m)

# compute fraction of variance kept for each target dimension k
var <- cumsum(vars)
var <- var/var[length(var)]

# output
L <- list("points" = reduced, "variables" = vec, "cumulativevariance" = var, "spectrum" = vars)

return(L)
}
