import shapefile  #Should install pyshp moudle
import pandas as pd
from pyproj import Proj, transform #Should install pyproj module


#read data 
shp_path_node = './mapData/MOCT_NODE.shp'
sf_node = shapefile.Reader(shp_path_node)
shp_path_link = './mapData/MOCT_LINK.shp'
sf_link = shpaefile.Reader(shp_path_link)

sf_node
