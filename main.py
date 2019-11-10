from csvsGenerator import csvsGenerator
from data.sklearnDatasets import no_structure, blobs, aniso, varied, noisy_moons, noisy_circles
from data.customCircunferencesDataset import customCircunferencesDataset
from config import resourcesFolder
from ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
from datasetDrawer import plotDatasets

# save all the generated data sets together
datasets = [
    ({'k': '2', 'name': 'noisy_circles'}, noisy_circles),
    ({'k': '2', 'name': 'noisy_moons'}, noisy_moons),
    ({'k': '3', 'name': 'varied'}, varied),
    ({'k': '3', 'name': 'aniso'}, aniso),
    ({'k': '3', 'name': 'blobs'}, blobs),
    ({'k': '2', 'name': 'no_structure'}, no_structure),
    ({'k': '2', 'name': 'customCircunferencesDataset'}, customCircunferencesDataset)
    ] # think about what k would be proper for no_structure

# print the generated data sets
plotDatasets(datasets)
# store the generated datasets into csv files
csvsGenerator(datasets, resourcesFolder)
# obtain the data sets from the csv files
datasetsFormCsvFiles = ndarraysFormCsvsGenerator(resourcesFolder)
# print the fetched data sets
plotDatasets(datasetsFormCsvFiles)