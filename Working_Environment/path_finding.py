import osmnx as ox, networkx as nx, pandas as pd
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
# =============================================================================
# def SamplePath(dest):
#     path1 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
#     path2 = pd.DataFrame(columns=["location", 'latitude', 'longitude'])
#     #홀수, 짝수에 따라 임의로 배송지 결정.
#     for i in dest.index:
#         lst = [dest.loc[i][0], dest.loc[i][1], dest.loc[i][2]]
#         if i%2 == 0:
#             path1.loc[len(path1)] = lst
#         else:
#             path2.loc[len(path2)] = lst
# 
#     #경로 반환
#     return path1, path2
# =============================================================================

#배정된 배송지들 사이의 경로 찾기.
def findRoute(G, dist): 
    del dist[0]
    routes = []
    for i in range(len(dist)-1):
        orig_node = ox.get_nearest_node(G,(dist[i][1][0], dist[i][1][1]))
        after_node = ox.get_nearest_node(G,(dist[i+1][1][0], dist[i+1][1][1]))
        route = nx.shortest_path(G, orig_node, after_node, weight ='length')
        if i != 0:
            del route[0]
        routes += route
    return routes

#분배된 경로 한번에 보여주기.
def showPathAll(G, routes, colors = ['r','b']):
    ox.plot_graph_routes(G, routes, route_colors = colors, node_size = 0)

#분배된 경로 각각 저장.
def savePath(G, routes, fileNames): # paths):
    for i in range(len(routes)):
        m = ox.plot_route_folium(G, routes[i], node_size = 0, popup_attribute = 'length')
        #markOnMap(paths[i], m)
        m.save('./route/'+fileNames[i]+'.html')

#거리에 따른 분류
def task_dist(G, dest):
    n = int(input('배송원 수를 입력하세요: '))

    hub_x,hub_y = input('시작 위치를 입력하세요 ex) 36.015380, 129.369903 : ').split(',')
    
    #허브 위치
    orig_node = ox.get_nearest_node(G,(float(hub_x),float(hub_y)))

    #배송원 분배 리스트
    distribution =[]
    for i in range(n):
        distribution.append([])
        info = "배송원 {}".format(i+1)
        distribution[i].append(info)


    
    point = []      #도착지 정보 저장
    num = 0

    #도착지 정보 리스트로 추가 ex) location,latitude,longitude
    for i in dest.index:
        sub_lat = dest.loc[i,'latitude']
        sub_long = dest.loc[i,'longitude']
        title = dest.loc[i,'location']
        point.append([])
        point[num].append((title))
        point[num].append((sub_lat,sub_long))
        num+=1
    
    num = 0

    #도착지 정보 추가 - 허브로부터의 거리 추가 ex) location,latitude,longitude,length
    for i in point:
        after_node = ox.get_nearest_node(G,point[num][1])
        len =  nx.shortest_path_length(G, orig_node, after_node, weight ='length')/1000
        point[num].append(len)
        num+=1
    
    #거리에 따른 정렬
    point.sort(key=lambda x:x[2])
   

    #거리가 먼 순서대로 분배
    num =0
    while point:
        distribution[num%n].append(point.pop())
        num+=1
    
    #출력
    #for i in distribution:
        #print(i)
    return distribution

#메인함수
def main():
    dst = read_data('./dst/destination.csv')
    G = mkGraph('포항시 경상북도 대한민국')
    m = mkMap(36.031437, 129.402948)
    markOnMap(dst, m)
    save_map(m, './init/s_init.html')
    m1 = mkEGmap(G)
    markOnMap(dst, m1)
    save_map(m1, './init/init.html')
    dist_task = task_dist(G, dst)
    
    routes = []
    
    for dist in dist_task:
        route = findRoute(G, dist)
        routes.append(route)
    
    
    savePath(G,routes, ['r1','r2']) #, paths)
    
    
    
main()  

