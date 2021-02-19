# -*- coding: utf-8 -*-
import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt
import matplotlib as mpl
ox.config(use_cache=True, log_console=True)
ox.__version__

#원하는 지역 정보 가져오기
G = ox.graph_from_place("포항시, 경상북도, 대한민국", network_type='drive')
#지역 확인
#fig, ax = ox.plot_graph(G, figsize=(12,12), node_size=0, edge_linewidth=0.5)

#출발지, 목적지 설정
orig = list(G)[0]
dest = list(G)[120]

#거리 최단 경로 탐색
route = ox.shortest_path(G, orig, dest, weight ='length')
fig, ax = ox.plot_graph_route(G,route, route_color='y', route_linewidth=6, node_size=0.5)
route_graph_map = ox.plot_route_folium(G, route, popup_attribute='length')
route_graph_map.save('nodeMap.html')
