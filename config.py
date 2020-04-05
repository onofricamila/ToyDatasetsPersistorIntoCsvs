import json

paths = None
realDatasetName = None

def _getPaths():
    return paths


def _fetchConfig():
    # we use the global key word to be able to change the values of the variables declared outside the function
    global paths
    global realDatasetName

    configFilePath = "/home/camila/Desktop/TESIS/DATA/config.json"
    with open(configFilePath) as f:
        data = json.load(f)
    # fill variables
    paths = data.get("paths")
    realDatasetName = data.get("realDatasetName")


def _fetchElementIfNull(_getter):
    element = _getter()
    if (element != None):
        return element
    # else
    _fetchConfig()
    return _getter()


def _getElementFromDict(key, _getter):
    dict = _fetchElementIfNull(_getter)
    return dict.get(key)


def _getRealDatasetName():
    return realDatasetName


def getNonTimeSeriesDatasetsPath():
    return _getElementFromDict(key="nonTimeSeriesDatasetsPath", _getter=_getPaths)


def getTimeSeriesDatasetsPath():
    return _getElementFromDict(key="timeSeriesDatasetsPath", _getter=_getPaths)


def getRealToyDatasetName():
    return _fetchElementIfNull(_getRealDatasetName)





