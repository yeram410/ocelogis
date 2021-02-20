import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt, pandas as pd
import matplotlib as mpl
import folium
ox.config(use_cache=True, log_console=True)
ox.__version__

#포항시 도로 정보 그래프로 만들기. 
def mkMap(x, y):
    m = folium.Map(location = [x, y], zoom_start = 12)
    return m

def mkGraph(place, Ntype = 'drive'):
    G = ox.graph_from_place(place, network_type=Ntype)
    return G

#배송지 정보 불러오기
def read_data(fileName):
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

#도로정보 그래프로 지도에 표시
def mkEGmap(graph):
    m = ox.plot_graph_folium(graph)
    return m

#지도에 배송 목적지 마크
def markOnMap(destinations, m):
    #각 배송지의 위도, 경도, 목적지 이름 이용.    
    for i in destinations.index:
        sub_lat = destinations.loc[i,'latitude']
        sub_long = destinations.loc[i,'longitude']
        title = destinations.loc[i,'location']
        #지도에 데이터 찍기
        folium.Marker([sub_lat,sub_long], tooltip=title).add_to(m)

#지도 파일로 저장.
def save_map(m, filename):
    m.save(filename)

#def find_path():

#샘플 경로 생성.
def SamplePath(dest):
    path1 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
    path2 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
    #홀수, 짝수에 따라 임의로 배송지 결정.
    for i in dest.index:
        lst = [dest.loc[i][0], dest.loc[i][1], dest.loc[i][2]]
        if i%2 == 0:
            path1.loc[len(path1)] = lst
        else:
            path2.loc[len(path2)] = lst

    #경로 반환
    return path1, path2

#배정된 배송지들 사이의 경로 찾기.
def findRoute(G, path):
    routes = []
    for i in range(len(path)-1):
        orig_node = ox.get_nearest_node(G,(path.loc[i][1], path.loc[i][2]))
        after_node = ox.get_nearest_node(G,(path.loc[i+1][1], path.loc[i+1][2]))
        route = nx.shortest_path(G, orig_node, after_node, weight ='length')
        if i != 0:
            del route[0]
        routes += route
    return routes

#분배된 경로 한번에 보여주기.
def showPathAll(G, routes, colors = ['r','b']):
    ox.plot_graph_routes(G, routes, route_colors = colors, node_size = 0)

#분배된 경로 각각 저장.
def savePaths(G, routes, fileNames, paths):
    for i in range(len(routes)):
        m = ox.plot_route_folium(G, routes[i], node_size = 0, popup_attribute = 'length')
        markOnMap(paths[i], m)
        m.save('./route/'+fileNames[i]+'.html')

def savePath(G, route, fileName, paths):
    m = ox.plot_route_folium(G, route, node_size = 0, popup_attribute = 'length')
    markOnMap(paths, m)
    m.save('./route/'+fileName+'.html')
#메인함수
def main():
    dst = read_data('./dst/destination3.csv')
    G = mkGraph('포항시 경상북도 대한민국')
    
    #for sample test
    route = findRoute(G, dst)
    savePath(G, route, 'new_sr', dst)
    
    
    
main()  

