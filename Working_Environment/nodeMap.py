import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString
from descartes import PolygonPatch
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
ox.config(use_cache=True, log_console=True)
ox.__version__


G = ox.graph_from_place('경상북도, 대한민국', network_type='drive', simplify=False)
#fig, ax = ox.plot_graph(G, figsize=(12,12), node_size=0, edge_linewidth=0.5)

G_proj = ox.project_graph(G)

orig_node = ox.get_nearest_node(G, (36.104095, 129.391966))
dest_node = ox.get_nearest_node(G, (35.870975, 128.594533))


import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns 
#%matplotlib inline
plt.rcParams["figure.figsize"] = (20,20)

#최단경로 표시
route = nx.shortest_path(G, orig_node, dest_node, weight = 'length')
fig, ax = ox.plot_graph_route(G, route, node_size = 0, figsize=(20,20))

#최단경로 거리 확인
len = nx.shortest_path_length(G, orig_node, dest_node, weight = 'length') / 1000
print(round(len, 1), "킬로미터")

# =============================================================================
# #Folium 웹맵에 시각화
# rroute_graph_map = ox.plot_route_folium(G, route,
#        route_map=graph_map, popup_attribute='length')
# ox.plot_route_folium()
# route_graph_map.save('nodeMap.html')
# =============================================================================
