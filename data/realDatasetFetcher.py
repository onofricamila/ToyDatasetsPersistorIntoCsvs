from config import getTimeSeriesDatasetsPath, getRealToyDatasetName, getRealDatasetPath
from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import pandas as pd
import numpy as np

def prepareRealDataset():
    originalDatasetFile = getRealDatasetPath()
    targetFolder = getTimeSeriesDatasetsPath()
    targetFileName = getRealToyDatasetName() + ".csv"

    dataFrame = pd.read_csv(originalDatasetFile, sep=',')
    dataFrame.columns = ['to_timestamp', 'latitude', 'longitude', 'car_id']
    dataFrame['to_timestamp'] = dataFrame['to_timestamp'].astype('datetime64[ns]')
    dataFrame = dataFrame[(dataFrame.latitude != 0) & (dataFrame.longitude != 0)]
    dataFrameSortedByTimestamp = dataFrame.sort_values(by="to_timestamp")
    resultantDataframe = dataFrameSortedByTimestamp[["latitude","longitude"]]
    resultantDataframe.to_csv(targetFolder+targetFileName, header=False, index=False)






    # Create heatmap of locations with stops and distribution of stop times
    print("Plotting heatmap of all gps coordinates and displaying it centered around Gothenburg")
    import folium
    from folium import Choropleth, Circle, Marker
    from folium.plugins import HeatMap, MarkerCluster

    def embed_map(m, file_name):
        from IPython.display import IFrame
        m.save(file_name)
        return IFrame(file_name, width='100%', height='500px')

    # Create a base map
    m_5 = folium.Map(location=[57.7057749, 11.972196], tiles='cartodbpositron', zoom_start=10)
    # Add a heatmap to the base map
    HeatMap(data=resultantDataframe, radius=10).add_to(m_5)
    # Display the map
    print("Map written to heatMap.html")
    embed_map(m_5, 'heatMap.html')




    # gothenburg NASA like static map
    # NWCorner = [57.965252, 11.388828]
    # SWCorner = [57.472575, 12.411249]
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    map = Basemap(llcrnrlon=11.388828, llcrnrlat=57.472575, urcrnrlon=12.411249, urcrnrlat=57.965252, epsg=5520)
    # http://server.arcgisonline.com/arcgis/rest/services
    map.arcgisimage(service='World_Street_Map', xpixels=15000, verbose=True)
    map.scatter([57.7], [11.5], c='r')
    plt.show()





    # ejemplo de como hacer un mapa en blanco y negro con puntitos
    plt.figure(1)
    map = Basemap(projection='merc',
                  resolution='l',
                  llcrnrlat=50,
                  llcrnrlon=5,
                  urcrnrlat=60,
                  urcrnrlon=20)
    map.drawmapboundary(fill_color='aqua')
    map.drawcoastlines()
    map.drawcountries(color='#ffffff', linewidth=0.5)
    map.fillcontinents(color='gray', lake_color='aqua')

    long = np.array([13.404954, 11.581981, 9.993682, 8.682127, 6.960279,
                     6.773456, 9.182932, 12.373075, 13.737262, 11.07675,
                     7.465298, 7.011555, 12.099147, 9.73201, 7.628279,
                     8.801694, 10.52677, 8.466039, 8.239761, 10.89779,
                     8.403653, 8.532471, 7.098207, 7.216236, 9.987608,
                     7.626135, 11.627624, 6.852038, 10.686559, 8.047179,
                     8.247253, 6.083887, 7.588996, 9.953355, 10.122765])

    lat = np.array([52.520007, 48.135125, 53.551085, 50.110922, 50.937531,
                    51.227741, 48.775846, 51.339695, 51.050409, 49.45203,
                    51.513587, 51.455643, 54.092441, 52.375892, 51.36591,
                    53.079296, 52.268874, 49.487459, 50.078218, 48.370545,
                    49.00689, 52.030228, 50.73743, 51.481845, 48.401082,
                    51.960665, 52.120533, 51.47512, 53.865467, 52.279911,
                    49.992862, 50.775346, 50.356943, 49.791304, 54.323293])

    colors = np.array([2.72189792, 3.62138986, 1.7947676, 1.36524602, 1.75664228,
                       3.0777491, 2.39580451, 1.17822874, 1.35503558, 2.28517658,
                       3.66472978, 1.76467741, 0.72551119, 1.76997962, 4.49420944,
                       2.34434288, 1.3243405, 2.35945794, 3.16147488, 2.94025564,
                       1.68774158, 0.67602518, 1.60727613, 1.85608281, 3.57769226,
                       1.33501838, 3.32549868, 2.95492675, 2.83391381, 2.33983198,
                       2.59607424, 1.24260218, 1.89258818, 2.07508363, 3.03319927])

    x, y = map(long, lat)
    map.plot(x, y, 'o', c='r')
    plt.show()


# =======
# from config import getTimeSeriesDatasetsPath, getRealToyDatasetName
# from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
# import pandas as pd
#
# def prepareRealDataset():
#     originalDatasetFile = "/home/camila/Desktop/TESIS/Datasets/Trayectorias - Taxis/California_all_dataset.csv"
#     targetFolder = getTimeSeriesDatasetsPath()
#     targetFileName = getRealToyDatasetName() + ".csv"
#
#     dataFrame = pd.read_csv(originalDatasetFile, sep=';')
#     dataFrame['to_timestamp'] = dataFrame['to_timestamp'].astype('datetime64[ns]')
#     dataFrameSortedByTimestamp = dataFrame.sort_values(by="to_timestamp")
#     resultantDataframe = dataFrameSortedByTimestamp[["latitude","longitude"]]
#     resultantDataframe.to_csv(targetFolder+targetFileName, header=False, index=False)
# >>>>>>> ba636c7ca51c83fecd72d6ae735040c1f6a4fe7b
