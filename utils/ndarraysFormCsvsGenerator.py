import numpy as np
import os
from sys import exit
import csv

def ndarraysFormCsvsGenerator(resourcesFolder):
    # try to get a list of all the files inside the specified folder
    try:
        files = os.listdir(resourcesFolder) # returns a list with all the files names inside the specified folder
    except BaseException as e:
        print("Could not open resources folder: " + str(e))
        exit()
    # for saving all the fetched data sets together
    datasets = []
    # iterate over the list of files
    for fileFullName in files:
        filePath = resourcesFolder + fileFullName
        # get the k param from header
        with open(filePath, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)  # gets the first line
        k = header[0] # 'header' returns ['k',]
        # get the data
        ndarray = np.genfromtxt(filePath, delimiter=",", skip_header=1) # header must be skipped
        fileNameWithoutExtension = fileFullName.split(".")[0]
        # append info to datasets
        datasets.append((
            {'k': k, 'name': fileNameWithoutExtension}, ndarray
        ))
    return datasets
    
