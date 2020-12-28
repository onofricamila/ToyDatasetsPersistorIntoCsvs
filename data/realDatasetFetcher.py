from config import getTimeSeriesDatasetsPath, getRealToyDatasetName, getRealDatasetPath
from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import pandas as pd
import numpy as np


def prepareRealDataset():
    originalDatasetFile = getRealDatasetPath()
    targetFolder = getTimeSeriesDatasetsPath()
    targetFileName = getRealToyDatasetName() + ".csv"

    dataFrame = pd.read_csv(originalDatasetFile, sep=',')
    dataFrame.columns = ['to_timestamp', 'longitude', 'latitude', 'car_id']
    dataFrame['to_timestamp'] = dataFrame['to_timestamp'].astype('datetime64[ns]')
    dataFrame = dataFrame[(dataFrame.latitude != 0) & (dataFrame.longitude != 0)]
    dataFrameSortedByTimestamp = dataFrame.sort_values(by="to_timestamp")
    resultantDataframe = dataFrameSortedByTimestamp           # antes subseteabamos [["latitude","longitude"]]
    resultantDataframe[:3223404].to_csv(targetFolder+targetFileName, header=True, index=False) # hardcodeo la cantidad de rows que quiero
    return resultantDataframe

