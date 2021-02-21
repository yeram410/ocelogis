#CLA
import networkx as nx
import osmnx as ox
import pandas as pd
############################################

def checkconnect( init, final, graph):
	traveled = [] # List of nodes we have already checked.
    
	while True:
		check = 0 # Initiate control flow variable
		# list which holds nodes connected to the initial node.
		traveled.append(init)
		# imm is a list of immediate neighbors to the initial node.
		imm = graph.neighbors(init)
		
		# If the node has no connected neighbors, we immediately know
		# it is valid.
		if len(imm) == 0:
			return 1
		
		for i in range(len(traveled)):
			if imm[0] == traveled[i]:
				imm.pop(0)
				break
			if len(imm) > 2:	
				if imm[1] == traveled[i]:
					imm.pop(1)
					break
		
		for i in range(len(traveled)):
			if final == traveled[i]:
				# This means that we have connected the initial
				# to the desired final node and an edge placement is
				# illegal.
				check = 1 # Set the control flow variable to 1.
		if check == 1:
			return 0;
		if len(imm) > 0:
			init = imm[0]
		else:
			return 1

###################3


def cla(marked_list, G):
    matrix = {}

    #배송지 노드로 변환
    node_list = []
    for mark in marked_list:
        node = ox.get_nearest_node(G, mark[1], mark[2])
        node_list.append(node)


    #각 노드 연결하는 edge weight 구하고 매트릭스 만들기.
    for i in range(len(node_list)):
        matrix[i] = {}
        for j in range(len(node_list)):
            w = nx.shortest_path(G, node[i], node[j])
            matrix[i][j] = w
      
#코스트 계산
    cost = 0
                    
    #이미 방문한 노드
    visited = []
    #그래프 엣지 없이 그리기.
    chart = nx.Graph()
    for node in node_list:
        chart.add_node(node)
        
        for k in range(len(node_list)):
            cheapest = float('inf')
            #chea6pest link 찾기
            for i in range(len(matrix)):    # or node_list
                for j in range(len(matrix)):
                    if matrix[i][j] < cheapest:
                        if(chart.has_edge(i, j) == False):
                            cheapest = matrix[i][j]
                            init = i
                            final = j
    
    #chart에 cheapest edge 그리기.
        chart.add_edge(init, final, weight = matrix[init][final])
        cost = cost + matrix[init][final]
        #chart3.add_ede(init, final)
        visited.append(init)
        visited.append(final)
        
        circuit = checkconnect(init, final, chart)
        
        if chart.degree(init) < 2 and chart.degree(final) < 2 and circuit == 1:
            cost += cheapest # Calculate the new tour length
            chart.add_edge(init, final, weight = matrix[init][final])
            visited.append(init) # List of nodes we have been to. 
            visited.append(final)
            #traveled3 = list(set(traveled3))
            #else:
                #chart.add_edge(init, final)
        

def main():
    G = ox.graph_from_place('포항시 경상북도 대한민국', network_type='drive')
    marked_list = pd.read_csv('./dst/destination')
    cla(marked_list, G)

