# -*- coding: utf-8 -*-
# =============================================================================
# import pandas as pd
# import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt
# import seaborn as sb
# import matplotlib as mpl
# import folium
# ox.config(use_cache=True, log_console=True)
# ox.__version__
# =============================================================================

# =============================================================================
# #전체 엣지 folium에 표현.
# place = 'Liverpool, United Kingdom'
# graph = ox.graph_from_place(place, network_type='drive')
# nodes, streets = ox.graph_to_gdfs(graph)
# m = ox.plot_graph_folium(graph)
# m.save('edges.html')
# =============================================================================


# =============================================================================
# 
# #street_types = pd.DataFrame(edges["highway"].apply(pd.Series)[0].value_counts().reset_index())
# 
# style = {'color': '#F7DC6F', 'weight':'1'}
# m = folium.Map([-2.914018, 53.366925], zoom_start=15, tiles='CartoDb dark_matter')
# folium.GeoJson(streets.sample(), style_function=lambda x: style).add_to(m)
# m.save('edges.html')
# m
# =============================================================================


# =============================================================================
# #sample path를 위한 df 나누기
# dst = pd.read_csv('destination.csv')
# 
# t1 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
# t2 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
# 
# for i in dst.index:
#     lst = [dst.loc[i][0], dst.loc[i][1], dst.loc[i][2]]
#     if i%2 == 0:
#         t1.loc[len(t1)] = lst
#     else:
#         t2.loc[len(t2)] = lst
# =============================================================================

# =============================================================================
# G = ox.graph_from_place('포항시, 경상북도, 대한민국')
# m = ox.plot_graph_folium(G[36.103197, 129.391725])
# m.save('graphTst.html')
#  
# =============================================================================

# =============================================================================
# #루트 합치기
# import osmnx as ox
# import networkx as nx
# import plotly.graph_objects as go
# import numpy as np
# import folium
# ox.config(use_cache=True, log_console=True)
# ox.__version__
# 
# 
# #원하는 지역 표시
# city = ox.graph_from_place('북구, 포항시, 경상북도, 대한민국')
# ox.plot_graph(ox.project_graph(city))
# 
# #출발지, 도착지 노드 찾기
# orig_node = ox.get_nearest_node(city, (36.102960, 129.391312))
# dest_node = ox.get_nearest_node(city, (36.080058, 129.393611))
# 
# dest_node2 = ox.get_nearest_node(city, (36.062193, 129.381536))
# 
# #최단거리 분석
# route = nx.shortest_path(city, orig_node, dest_node, weight = 'length')
# route2 = nx.shortest_path(city, dest_node, dest_node2, weight = 'length')
# 
# #루트 여러개 하나로 묶기.
# del route2[0]
# routes = route+route2
# print('route')
# print(route)
# print()
# print('routes')
# print(routes)
# #fig, ax = ox.plot_graph_route(city, route2, node_size = 0)
# 
# #fig, ax = ox.plot_graph_routes(city, routes, node_size=0)
# #m = ox.plot_route_folium(city, routes, node_size = 0)
# 
# m = ox.plot_route_folium(city, routes)
# 
# m.save('basic.html')
# =============================================================================


#루트 합치기
import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import folium
ox.config(use_cache=True, log_console=True)
ox.__version__

# =============================================================================
# =============================================================================
# # #원하는 지역 표시
# # city = ox.graph_from_place('북구, 포항시, 경상북도, 대한민국')
# # ox.plot_graph(ox.project_graph(city))
# # 
# # #출발지, 도착지 노드 찾기
# # orig_node = ox.get_nearest_node(city, (36.102960, 129.391312))
# # dest_node = ox.get_nearest_node(city, (36.080058, 129.393611))
# # 
# # dest_node2 = ox.get_nearest_node(city, (36.062193, 129.381536))
# # 
# # #최단거리 분석
# # route = nx.shortest_path(city, orig_node, dest_node, weight = 'length')
# # route2 = nx.shortest_path(city, dest_node, dest_node2, weight = 'length')
# # 
# # 
# # 
# # m = ox.plot_route_folium(city, route )
# # ox.plot_route_folium(city, route2).add_to(m)
# =============================================================================
# =============================================================================
#fig.add_to(m)
#ax.add_to(m)
#ox.plot_graph_route(city, route2).add_to(m)
# Add the same marker to both maps:
    
# =============================================================================
# fg = folium.FeatureGroup()
# g1 = folium.FeatureGroupSubGroup(fg, 'g1')  # First subgroup of fg
# g2 = folium.plugins.FeatureGroupSubGroup(fg, 'g2')  # Second subgroup of fg
# m.add_child(fg)
# m.add_child(g1)
# m.add_child(g2)
# g1.add_child(folium.Marker([0,0]))
# g2.add_child(folium.Marker([0,1]))
# folium.LayerControl().add_to(m) 
# =============================================================================

#fig, ax = ox.plot_graph_route(city, route2, node_size = 0)

#fig, ax = ox.plot_graph_routes(city, routes, node_size=0)
#m = ox.plot_route_folium(city, routes, node_size = 0)

#m = ox.plot_route_folium(city, routes)
#m.save('basic.html')

#node, edge = city

G = ox.graph_from_place('북구, 포항시, 경상북도, 대한민국', network_type = 'drive')
nodes, edges = ox.graph_to_gdfs(G)
edges.to_csv("edge_inform.csv")



