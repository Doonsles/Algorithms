import heapq


graph1 = {}
graph1['A'] = ['C', 'B']
graph1['B'] = []
graph1['C'] = []

edge_weights1 = {}
edge_weights1['A', 'B'] = 5
edge_weights1['B', 'A'] = 5
edge_weights1['A', 'C'] = 4
edge_weights1['C', 'A'] = 4

graph2 = {}
graph2['A'] = ['B', 'C']
graph2['B'] = ['D']
graph2['C'] = ['E']
graph2['D'] = ['F', 'G']
graph2['E'] = ['D']
graph2['F'] = ['E']
graph2['G'] = ['F']

edge_weights2 = {}
edge_weights2['A', 'B'] = 9
edge_weights2['A', 'C'] = 8
edge_weights2['B', 'D'] = 7
edge_weights2['C', 'E'] = 3
edge_weights2['E', 'D'] = 2 
edge_weights2['D', 'G'] = 4 
edge_weights2['D', 'F'] = 5
edge_weights2['G', 'F'] = 1
edge_weights2['F', 'E'] = 6


graph3 = {}
graph3['A'] = ['C', 'B']
graph3['B'] = ['C', 'D', 'E']
graph3['C'] = ['B', 'D', 'E']
graph3['D'] = []
graph3['E'] = ['D']

edge_weights3 = {}
edge_weights3['A', 'C'] = 2
edge_weights3['A', 'B'] = 4
edge_weights3['C', 'B'] = 1
edge_weights3['B', 'C'] = 3
edge_weights3['C', 'E'] = 5
edge_weights3['C', 'D'] = 4
edge_weights3['B', 'D'] = 2
edge_weights3['B', 'E'] = 3 
edge_weights3['E', 'D'] = 1


#pseudocode from Algorithms by S. Dasgupta, C.H. Papadimitriou, and U.V. Vazirani 
#procedure dijkstra(G, l, s)
#Input: Graph G = (V, E), directed or undirected;
#positive edge lengths {le : e in E}; vertex s in V 
#Output: For all vertices u reachable from s, dist(u) is set to the distance from s to u.
#for all u in V : dist(u) = infinity
#prev(u) = nil 
#dist(s) = 0
#H = makequeue (V) (using dist-values as keys) 
#while H is not empty:
#u = deletemin(H)
#for all edges (u, v) in E:
#if dist(v) > dist(u) + l(u, v): 
#dist(v) = dist(u) + l(u, v) 
#prev(v) = u 
#decreasekey(H, v)

def dijkstra (graph, edge_weights, start_node):
    
    distance = {}
    prev = {}
    
    for u in graph:
        distance[u] = float("inf")
        prev[u] = None

    removed = {} 
    
    distance[start_node] = 0
    
    heap = []
    
    initial_edges = graph[start_node]

    for v in initial_edges:
        distance[v] = edge_weights[start_node, v]
        new_entry = (edge_weights[start_node, v],v)
        heapq.heappush(heap, new_entry)
 
    u = 0
    while heap:
    	u = heapq.heappop(heap)
        removed[u[1]] = 'R'
        for v in graph[u[1]]:
            if (distance[v] > distance[u[1]] + edge_weights[u[1], v]) and (not removed.has_key(v)):
                distance[v] = distance[u[1]] + edge_weights[u[1], v]
                prev[v] = u[1]
                heapq.heappush (heap, (distance[v],v))

    return distance                

print dijkstra (graph3, edge_weights3, 'A')

