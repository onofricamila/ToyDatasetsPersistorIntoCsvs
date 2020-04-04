from config import getTimeSeriesDatasetsPath
from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import pandas as pd

def prepareRealDataset():
    originalDatasetFile = "/home/camila/Desktop/TESIS/Datasets/Trayectorias - Taxis/dataset/Californa1.csv"
    targetFolder = getTimeSeriesDatasetsPath()
    targetFileName = "taxis.csv"

    dataFrame = pd.read_csv(originalDatasetFile, sep=';')
    # Preview the first 5 lines of the loaded data
    resultantDataframe = dataFrame[["latitude","longitude"]]
    resultantDataframe.to_csv(targetFolder+targetFileName, header=False, index=False)
