from utils.csvsGenerator import csvsGenerator
from data.sklearnDatasets import no_structure, blobs, aniso, varied, noisy_moons, noisy_circles
from data.customCircumferencesDatasetGenerator import custom_circumferences
from config import resourcesFolder, getNonTimeSeriesDatasetsPath, getTimeSeriesDatasetsPath
from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
from utils.datasetDrawer import plotDatasets

# save all the generated data sets together
non_time_series_datasets = [
    ({'k': '2', 'name': 'noisy_circles'}, noisy_circles),
    ({'k': '2', 'name': 'noisy_moons'}, noisy_moons),
    ({'k': '3', 'name': 'varied'}, varied),
    ({'k': '3', 'name': 'aniso'}, aniso),
    ({'k': '3', 'name': 'blobs'}, blobs),
    ({'k': '2', 'name': 'no_structure'}, no_structure),
    ] # think about what k would be proper for no_structure

non_time_series_datasets = sorted(non_time_series_datasets, key=lambda x: x[0]['name'])
time_series_datasets = [
     ({'k': '2', 'name': 'custom_circumferences'}, custom_circumferences)
    ]
# print the generated data sets
plotDatasets(non_time_series_datasets + time_series_datasets)
# store the generated datasets into csv files
csvsGenerator(non_time_series_datasets, getNonTimeSeriesDatasetsPath())
csvsGenerator(time_series_datasets, getTimeSeriesDatasetsPath())
# obtain the data sets from the csv files
non_time_series_datasets = ndarraysFormCsvsGenerator(getNonTimeSeriesDatasetsPath())
time_series_datasets = ndarraysFormCsvsGenerator(getTimeSeriesDatasetsPath())
# print the fetched data sets
plotDatasets(non_time_series_datasets + time_series_datasets)