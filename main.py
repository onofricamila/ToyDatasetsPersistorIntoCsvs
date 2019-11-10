from utils.csvsGenerator import csvsGenerator
from data.sklearnDatasets import no_structure, blobs, aniso, varied, noisy_moons, noisy_circles
from data.customCircumferencesDatasetGenerator import custom_circumferences
from config import resourcesFolder
from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
from utils.datasetDrawer import plotDatasets

# save all the generated data sets together
datasets = [
    ({'k': '2', 'name': 'noisy_circles'}, noisy_circles),
    ({'k': '2', 'name': 'noisy_moons'}, noisy_moons),
    ({'k': '3', 'name': 'varied'}, varied),
    ({'k': '3', 'name': 'aniso'}, aniso),
    ({'k': '3', 'name': 'blobs'}, blobs),
    ({'k': '2', 'name': 'no_structure'}, no_structure),
    ({'k': '2', 'name': 'custom_circumferences'}, custom_circumferences)
    ] # think about what k would be proper for no_structure

datasets = sorted(datasets, key=lambda x: x[0]['name'])

# print the generated data sets
plotDatasets(datasets)
# store the generated datasets into csv files
csvsGenerator(datasets, resourcesFolder)
# obtain the data sets from the csv files
datasetsFormCsvFiles = ndarraysFormCsvsGenerator(resourcesFolder)
# print the fetched data sets
plotDatasets(datasetsFormCsvFiles)