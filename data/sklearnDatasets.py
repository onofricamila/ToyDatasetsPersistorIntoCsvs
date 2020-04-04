from sklearn import datasets
import numpy as np

# IMPORTANT:
# labels are discarded --> we only wanna the points

# general config
n_samples = 1500
noise = 0.05

# circles
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5, noise=noise)[0]

# moons
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=noise)[0]

# blobs
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)[0]

# anisotropicly distributed data
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)[0]

# blobs with varied variances
varied = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state)[0]

