import numpy as np
import os
from sys import exit
from config import resourcesFolder

try:
    filesNames = os.listdir(resourcesFolder) # returns a list with all the files' names inside the specified folder
except BaseException as e:
    print("Could not open resources folder: " + str(e))
    exit()

# for saving all the fetched data sets together
datasets = []

for fileFullName in filesNames:
    ndarray = np.genfromtxt(resourcesFolder + '/' + fileFullName, delimiter=",")
    fileNameWithoutExtension = fileFullName.split(".")[0]
    datasets.append((fileNameWithoutExtension, ndarray))

print(datasets)