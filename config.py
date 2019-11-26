import json

csvDatasetsPath = None

def fetchConfig():
    # we use the global key word to being able to change the values of the variables declared outside the function
    global csvDatasetsPath

    configFilePath = "/home/camila/Desktop/TESIS/DATA/config.json"
    with open(configFilePath) as f:
        data = json.load(f)
    # fill variables
    csvDatasetsPath = data.get("csvDatasetsPath")


def getClusteringResultsPath():
    if csvDatasetsPath is not None:
        return csvDatasetsPath
    # else
    fetchConfig()
    return csvDatasetsPath

resourcesFolder = getClusteringResultsPath()
