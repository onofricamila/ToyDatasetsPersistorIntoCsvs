# ToyDatasetsPersistorIntoCsvs
Here, a way to persist generated toy datasets is provided. The idea is to make random datasets, like the ones generated using sklearn, persist, storing them into .csv files. This is really useful when comparing different machine learning algorithms, to avoid the random component.

* csvsGenerator.py --> takes the datasets from data.py -> datasets, and iterates over them to generate 1 csv file for each one

* ndarraysFormCsvsGenerator.py --> as a test, iterates over the files inside the resources folder to obtain ndarrays from the csvs
