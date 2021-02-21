import osmnx as ox, networkx as nx, geopandas as gpd, matplotlib.pyplot as plt, pandas as pd
import matplotlib as mpl
import folium
ox.config(use_cache=True, log_console=True)
ox.__version__

def task_dist():
    n = int(input('배송원 수를 입력하세요: '))

    hub_x,hub_y = input('시작 위치를 입력하세요 ex) 15,30 : ').split(',')
    
    dest = read_data('./destination.csv')
    G = mkGraph('포항시 경상북도 대한민국')
    
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
    for i in distribution:
        print(i)

#배송지 정보 불러오기
def read_data(fileName):
    dst = pd.read_csv(fileName)
    return dst

def mkGraph(place, Ntype = 'drive'):
    G = ox.graph_from_place(place, network_type=Ntype)
    return G

def main():
    task_dist()
main()
