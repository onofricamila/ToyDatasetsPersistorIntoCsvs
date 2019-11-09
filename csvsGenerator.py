from data import datasets
import numpy as np
import os
from config import resourcesFolder

if not os.path.exists(resourcesFolder):
    os.makedirs(resourcesFolder)

for i in range(len(datasets)):
    d = datasets[i][1]
    dName = datasets[i][0]
    dWithoutLabels = d[0]
    np.savetxt(resourcesFolder + '/' + dName + '.csv', dWithoutLabels, delimiter=',')