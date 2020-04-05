from config import getTimeSeriesDatasetsPath, getRealToyDatasetName
from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import pandas as pd

def prepareRealDataset():
    originalDatasetFile = "/home/camila/Desktop/TESIS/Datasets/Trayectorias - Taxis/dataset/Californa1.csv"
    targetFolder = getTimeSeriesDatasetsPath()
    targetFileName = getRealToyDatasetName() + ".csv"

    dataFrame = pd.read_csv(originalDatasetFile, sep=';')
    dataFrame['to_timestamp'] = dataFrame['to_timestamp'].astype('datetime64[ns]')
    dataFrameSortedByTimestamp = dataFrame.sort_values(by="to_timestamp")
    resultantDataframe = dataFrameSortedByTimestamp[["latitude","longitude"]]
    resultantDataframe.to_csv(targetFolder+targetFileName, header=False, index=False)
