import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.decomposition import PCA

# Preprocessing functions

def normalize_data(train, train_full, test):
    
    norm_train = (train - train.mean()) / train.std()
    norm_train_full = (train_full - train.mean()) / train.std()
    norm_test = (test - train.mean()) / train.std()
    
    return norm_train, norm_train_full, norm_test

def generate_PCA(train, train_full, test, n_components):
    
    pca = PCA(n_components = n_components, svd_solver = 'full')

    pca_train = pd.DataFrame(pca.fit_transform(train))
    pca_train.index = train.index
    
    pca_train_full = pd.DataFrame(pca.fit_transform(train_full))
    pca_train_full.index = train_full.index

    pca_test = pd.DataFrame(pca.transform(test))
    pca_test.index = test.index
    
    return pca_train, pca_train_full, pca_test


# Functions to calculate Mahalanobis Distance

def inv_cov_matrix(x):
    cov = np.cov(x.T)
    if np.all(np.linalg.eigvals(cov) > 0):
        return(np.linalg.inv(cov))

def calculate_M_distance(inv_cov_matrix, means, data):
    diff = data - means
    md = []
    for i in range(len(diff)):
        md.append(np.sqrt(diff[i].dot(inv_cov_matrix).dot(diff[i])))
    return md

def detect_outliers(dist, extreme=False, verbose=False):
    k = 3. if extreme else 2.
    threshold = np.mean(dist) * k
    outliers = []
    for i in range(len(dist)):
        if dist[i] >= threshold:
            outliers.append(i)
    return np.array(outliers)

def calculate_threshold(dist, extreme=False, verbose=False):
    k = 3. if extreme else 2.
    threshold = np.mean(dist) * k
    return threshold


# Plotting functions

def plot_distances(anomalies):
    plt.figure(figsize=(15, 6))
    sns.distplot(anomalies,
                bins = 400)
    plt.xlim([0.0,15])
    plt.xlabel('Mahalanobis Dist')

def plot_detections(pred, true):

    pred.plot(figsize = (15,6), color = ['blue','red'], legend = True)

    anoms = list(true.index[true == 1])
    for a in anoms:
        plt.axvline(a, color='orange', alpha=0.02)