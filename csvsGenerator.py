from data import datasets
import numpy as np

for i in range(len(datasets)):
    d = datasets[i][1]
    dName = datasets[i][0]
    dWithoutLabels = d[0]
    np.savetxt('./resources/' + dName + '.csv', dWithoutLabels, delimiter=',')