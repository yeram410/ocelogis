import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString
from descartes import PolygonPatch
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
ox.config(use_cache=True, log_console=True)
ox.__version__

G = ox.graph_from_place('경상북도, 대한민국', network_type='drive', simplify=False)
fig, ax = ox.plot_graph(G, figsize=(12,12), node_size=0, edge_linewidth=0.5)    