import json

csvDatasetsPath = None
timeSeriesDatasetsPath = None
nonTimeSeriesDatasetsPath = None

def fetchConfig():
    # we use the global key word to being able to change the values of the variables declared outside the function
    global csvDatasetsPath
    global timeSeriesDatasetsPath
    global nonTimeSeriesDatasetsPath

    configFilePath = "/home/camila/Desktop/TESIS/DATA/config.json"
    with open(configFilePath) as f:
        data = json.load(f)
    # fill variables
    csvDatasetsPath = data.get("csvDatasetsPath")
    timeSeriesDatasetsPath = data.get("timeSeriesDatasetsPath")
    nonTimeSeriesDatasetsPath = data.get("nonTimeSeriesDatasetsPath")


def getCsvDatasetsPath():
    if csvDatasetsPath is not None:
        return csvDatasetsPath
    # else
    fetchConfig()
    return csvDatasetsPath


def getNonTimeSeriesDatasetsPath():
    if nonTimeSeriesDatasetsPath is not None:
        return nonTimeSeriesDatasetsPath
    # else
    fetchConfig()
    return nonTimeSeriesDatasetsPath


def getTimeSeriesDatasetsPath():
    if timeSeriesDatasetsPath is not None:
        return timeSeriesDatasetsPath
    # else
    fetchConfig()
    return timeSeriesDatasetsPath


resourcesFolder = getCsvDatasetsPath()
