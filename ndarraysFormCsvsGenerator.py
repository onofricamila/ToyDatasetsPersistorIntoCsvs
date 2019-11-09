import numpy as np
import os

resourcesFolderRelativeRoute = "./resources"
files = os.listdir(resourcesFolderRelativeRoute) # returns a list with all the files' names inside the specified folder

# for saving all the fetched data sets together
datasets = []

for fileName in files:
    ndarray = np.genfromtxt(resourcesFolderRelativeRoute + '/' + fileName, delimiter=",")
    datasets.append(ndarray)

print(datasets)