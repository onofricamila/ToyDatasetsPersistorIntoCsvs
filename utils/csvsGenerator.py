import numpy as np
import os

def csvsGenerator(datasets, resourcesFolder):
    # check if resourcesFolder needs to be created
    if not os.path.exists(resourcesFolder):
        os.makedirs(resourcesFolder)
    # iterate over the generated datasets
    for i, (params, dataset) in enumerate(datasets):
        d = dataset
        dName = params['name']
        k = params['k'] # denotes the number of natural clusters
        targetFile = resourcesFolder + dName + '.csv'
        np.savetxt(targetFile, d, delimiter=',', header=k, comments='') # the comments arg is passed to avoid '#' in header

