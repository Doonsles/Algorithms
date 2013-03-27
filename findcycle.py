graph1 = {}
graph1['A'] = ['B']
graph1['B'] = ['C']
graph1['C'] = ['A']

graph2 = {}
graph2['A'] = ['B', 'C']
graph2['B'] = ['C', 'D']
graph2['C'] = ['E']
graph2['D'] = ['C']
graph2['E'] = ['D']

graph3 = {}
graph3['A'] = ['B', 'C']
graph3['B'] = ['C', 'D']
graph3['C'] = ['F']
graph3['D'] = ['C', 'E']
graph3['E'] = ['C']
graph3['F'] = []

pre = {}
post = {}
colors= {}
clock = 1

#pseudocode from Algorithms by S. Dasgupta, C.H. Papadimitriou, and U.V. Vazirani 
#procedure explore(G, v)
#Input: G = (V,E) is a graph; v in V
#Output: visited(u) is set to true for all nodes u reachable from v
#visited(v) = true 
#previsit(v)
#for each edge (v, u) in E:
#if not visited(u): explore(u) 
#postvisit(v)

def dfs(graph, start_node):
    
    previsit (start_node)
    list_to_visit = list(graph[start_node])
    
    while list_to_visit:
        node_to_visit = list_to_visit.pop(0)
        if not pre.has_key(node_to_visit):
            dfs(graph, node_to_visit)
    
    postvisit (start_node)


def previsit (v):
    global clock 
    pre[v] = clock
    clock = clock + 1

def postvisit (v):
    global clock
    post[v]= clock
    clock += 1


def find_cycle (graph):
    for u in graph:
        for v in graph[u]:
            #print vertex
            if ((pre[v] < pre[u]) and (post[u] < post[v])):
                print "There is a cycle! Vertex ", u, "is in the cycle."
                return
    print "There is no cycle in the test graph."

dfs(graph2, 'A')
find_cycle (graph2)

