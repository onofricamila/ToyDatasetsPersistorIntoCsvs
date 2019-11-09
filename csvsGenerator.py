from data import datasets
import numpy as np

for i in range(len(datasets)):
    d = datasets[i][0]
    np.savetxt('./resources/test' + str(i) + '.csv', d, delimiter=',')