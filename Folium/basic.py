# -*- coding: utf-8 -*-
import pandas as pd
import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt
import seaborn as sb
import matplotlib as mpl
import folium

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
dst = pd.read_csv('destination.csv')

t1 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
t2 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])

for i in dst.index:
    lst = [dst.loc[i][0], dst.loc[i][1], dst.loc[i][2]]
    if i%2 == 0:
        t1.loc[len(t1)] = lst
    else:
        t2.loc[len(t2)] = lst

