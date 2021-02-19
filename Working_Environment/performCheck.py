import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt, pandas as pd
import matplotlib as mpl
import folium
ox.config(use_cache=True, log_console=True)
ox.__version__

#포항시 도로 정보 그래프로 만들기. 
def mkGraph(place, Ntype = 'drive'):
    G = ox.graph_from_place(place, network_type=Ntype)
    return G

def readLoc(fileName):
    dst = pd.read_csv(fileName)
    return dst

# =============================================================================
# def mkFmap(destinations):
#     lat = destinations['latitude'].mean()
#     long = destinations['longitude'].mean()
#     #지도
#     m = folium.Map([lat,long],zoom_start=12)
#     return m
# =============================================================================

def mkEGmap(graph):
    m = ox.plot_graph_folium(graph)
    return m

def markOnMap(destinations, m):    
    for i in destinations.index:
        sub_lat = destinations.loc[i,'latitude']
        sub_long = destinations.loc[i,'longitude']
        title = destinations.loc[i,'location']
    #지도에 데이터 찍기
        folium.Marker([sub_lat,sub_long], tooltip=title).add_to(m)

def saveMap(m, filename):
    m.save(filename)

#def findPath(G, dest):

def SamplePath(dest):
    path1 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
    path2 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])

    for i in dest.index:
        lst = [dest.loc[i][0], dest.loc[i][1], dest.loc[i][2]]
        if i%2 == 0:
            path1.loc[len(path1)] = lst
        else:
            path2.loc[len(path2)] = lst

    return path1, path2

def findRoute(G, path):
    routes = []
    for i in range(len(path)-1):
        #orig = [ path.loc[i][1], path.loc[i][2] ]
        #after = [ path.loc[i][1], path.loc[i][2] ]
        orig_node = ox.get_nearest_node(G,(path.loc[i][1], path.loc[i][2]))
        after_node = ox.get_nearest_node(G,(path.loc[i+1][1], path.loc[i+1][2]))
        route = nx.shortest_path(G, orig_node, after_node, weight ='length')
        if i != 0:
            del route[0]
        routes += route
    return routes
        

def main():
    G = mkGraph('포항시 경상북도 대한민국')
    dst = readLoc('./dst/destination.csv')
    #m = mkFmap(dst)
    m1 = mkEGmap(G)
    markOnMap(dst, m1)
    saveMap(m1, 'check.html')
    
    #for sample test
    spth1, spth2 = SamplePath(dst)
    sroutes1 = findRoute(G, spth1)
    sroutes2 = findRoute(G, spth2)
   
    ox.plot_graph_routes(G,[sroutes1,sroutes2], route_colors = ['r', 'b'], node_size=0)
   
    #m2 = ox.plot_route_folium(G, sroutes1, node_size = 0, popup_attribute='length')
    #markOnMap(dst, m2)
    #m.save('multiple_path1.html')
    
    
main()  

