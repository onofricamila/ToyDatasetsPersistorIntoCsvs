# ToyDatasetsPersistorIntoCsvs
Here, a way to persist generated toy datasets is provided. The idea is to make random datasets, like the ones generated using sklearn, persist, storing them into .csv files. This is really useful when comparing different machine learning algorithms, to avoid the random component.

## How to try it
1. First, config the resources folder path in `config.py` (see the 'Important' section below)
2. Simply run the `main.py` file and you will how:
   * csvsGenerator.py --> takes the provided data sets and iterates over them to generate 1 csv file for each one
   * ndarraysFormCsvsGenerator.py --> as a test, iterates over the files inside the resources folder to obtain ndarrays from the csvs
   * datasetDrawer --> takes the given datas ets and plots them
   
## Which data sets are provided?
* a time series one, useful for stream simulation (customCircunferencesDataset)
* scikit-learn ...
   * noisy_circles
   * noisy_moons
   * varied
   * aniso
   * blobs
   * no_structure
   
## :grey_exclamation: Important: configuration
There is a `config` file, used to provide the _paths_ of the folders in which data will be stored. Those paths, have to be specified in a **json** file. This is done because many applicatios (developed in different languages) use the same folders. Here, a `config.json` example is shown:

```json
{
    "clusteringResultsPath": "/home/camila/Desktop/TESIS/DATA/clustering_results/",
    "csvDatasetsPath": "/home/camila/Desktop/TESIS/DATA/datasets/",
    "figuresPath": "/home/camila/Desktop/TESIS/DATA/figures/",
    "timeSeriesToyDatasetName": "custom_circumferences_without_k.csv",
    "algoNames": {
	"clustream": "CluStream",
	"denstream": "DenStream"
     }
}
```
**The path to the json file must be specified in the config file.**

   
