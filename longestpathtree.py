import heapq

graph1 = {}
graph1['A'] = ['B']
graph1['B'] = ['A', 'E']
graph1['C'] = ['D']
graph1['D'] = ['C', 'E', 'G']
graph1['E'] = ['B', 'D', 'F']
graph1['F'] = ['E']
graph1['G'] = ['D']


edgeweights1 = {}
edgeweights1['A', 'B'] = 450
edgeweights1['B', 'A'] = 450
edgeweights1['B', 'E'] = 1
edgeweights1['E', 'B'] = 1
edgeweights1['E', 'D'] = -1
edgeweights1['D', 'E'] = -1
edgeweights1['E', 'F'] = 3
edgeweights1['F', 'E'] = 3
edgeweights1['D', 'C'] = 50
edgeweights1['C', 'D'] = 50
edgeweights1['D', 'G'] = 1000
edgeweights1['G', 'D'] = 1000

graph2 = {}
graph2['A'] = ['B', 'C', 'D']
graph2['B'] = ['A', 'E', 'F', 'G']
graph2['C'] = ['A', 'H']
graph2['D'] = ['A', 'I', 'J']
graph2['E'] = ['B']
graph2['F'] = ['B']
graph2['G'] = ['B']
graph2['H'] = ['C']
graph2['I'] = ['D']
graph2['J'] = ['D']

edgeweights2 = {}
edgeweights2['A', 'B'] = 3
edgeweights2['B', 'A'] = 3 
edgeweights2['A', 'C'] = 5
edgeweights2['C', 'A'] = 5
edgeweights2['A', 'D'] = 7
edgeweights2['D', 'A'] = 7
edgeweights2['B', 'E'] = 4
edgeweights2['E', 'B'] = 4
edgeweights2['B', 'F'] = 9
edgeweights2['F', 'B'] = 9
edgeweights2['B', 'G'] = 8
edgeweights2['G', 'B'] = 8
edgeweights2['C', 'H'] = 1 
edgeweights2['H', 'C'] = 1 
edgeweights2['D', 'I'] = 2
edgeweights2['I', 'D'] = 2
edgeweights2['D', 'J'] = 6
edgeweights2['J', 'D'] = 6 


graph3 = {}
graph3['A'] = ['B', 'C', 'D']
graph3['B'] = ['A', 'E', 'F', 'G']
graph3['C'] = ['A', 'H']
graph3['D'] = ['A', 'I', 'J']
graph3['E'] = ['B', 'K', 'L', 'M']
graph3['F'] = ['B', 'O']
graph3['G'] = ['B', 'P']
graph3['H'] = ['C', 'Q']
graph3['I'] = ['D', 'R']
graph3['J'] = ['D', 'S', 'T', 'U', 'V', 'W', 'X']
graph3['K'] = ['E']
graph3['L'] = ['E']
graph3['M'] = ['E']
graph3['O'] = ['F']
graph3['P'] = ['G']
graph3['Q'] = ['H']
graph3['R'] = ['I']
graph3['S'] = ['J']
graph3['T'] = ['J']
graph3['U'] = ['J']
graph3['V'] = ['J'] 
graph3['W'] = ['J'] 
graph3['X'] = ['J'] 


edgeweights3 = {}
edgeweights3['A', 'B'] = 3
edgeweights3['B', 'A'] = 3
edgeweights3['A', 'C'] = 5
edgeweights3['C', 'A'] = 5
edgeweights3['A', 'D'] = 7
edgeweights3['D', 'A'] = 7
edgeweights3['B', 'E'] = 4
edgeweights3['E', 'B'] = 4
edgeweights3['B', 'F'] = 9
edgeweights3['F', 'B'] = 9
edgeweights3['B', 'G'] = 8
edgeweights3['G', 'B'] = 8
edgeweights3['C', 'H'] = 1
edgeweights3['H', 'C'] = 1
edgeweights3['D', 'I'] = 2
edgeweights3['I', 'D'] = 2
edgeweights3['D', 'J'] = 6
edgeweights3['J', 'D'] = 6
edgeweights3['E', 'K'] = 7
edgeweights3['K', 'E'] = 7
edgeweights3['E', 'L'] = 8
edgeweights3['L', 'E'] = 8
edgeweights3['E', 'M'] = 3
edgeweights3['M', 'E'] = 3
edgeweights3['F', 'O'] = 5
edgeweights3['O', 'F'] = 5
edgeweights3['G', 'P'] = 1
edgeweights3['P', 'G'] = 1
edgeweights3['H', 'Q'] = 4
edgeweights3['Q', 'H'] = 4
edgeweights3['I', 'R'] = 9
edgeweights3['R', 'I'] = 9
edgeweights3['J', 'S'] = 4
edgeweights3['S', 'J'] = 4
edgeweights3['J', 'T'] = 3
edgeweights3['T', 'J'] = 3
edgeweights3['J', 'U'] = 2
edgeweights3['U', 'J'] = 2
edgeweights3['J', 'V'] = 2
edgeweights3['V', 'J'] = 2
edgeweights3['J', 'W'] = 1
edgeweights3['W', 'J'] = 1
edgeweights3['J', 'X'] = 6
edgeweights3['X', 'J'] = 6

graph4 = {}
graph4['A'] = ['B', 'C', 'D', 'E']
graph4['B'] = ['A', 'F', 'G', 'H', 'I']
graph4['C'] = ['A', 'J']
graph4['D'] = ['A', 'K']
graph4['E'] = ['A', 'L', 'M', 'N', 'O']
graph4['F'] = ['B']
graph4['G'] = ['B']
graph4['H'] = ['B']
graph4['I'] = ['B']
graph4['J'] = ['C', 'P', 'Q', 'R', 'S']
graph4['K'] = ['D']
graph4['L'] = ['E']
graph4['M'] = ['E']
graph4['N'] = ['E']
graph4['O'] = ['E']
graph4['P'] = ['J']
graph4['Q'] = ['J']
graph4['R'] = ['J']
graph4['S'] = ['J']


edgeweights4 = {}
edgeweights4['A', 'B'] = 6
edgeweights4['B', 'A'] = 6
edgeweights4['A', 'C'] = 7
edgeweights4['C', 'A'] = 7
edgeweights4['A', 'D'] = 9
edgeweights4['D', 'A'] = 9
edgeweights4['A', 'E'] = 3
edgeweights4['E', 'A'] = 3
edgeweights4['B', 'F'] = 8
edgeweights4['F', 'B'] = 8
edgeweights4['B', 'G'] = 4
edgeweights4['G', 'B'] = 4
edgeweights4['B', 'H'] = 9
edgeweights4['H', 'B'] = 9
edgeweights4['B', 'I'] = 5
edgeweights4['I', 'B'] = 5
edgeweights4['C', 'J'] = 7
edgeweights4['J', 'C'] = 7
edgeweights4['D', 'K'] = 1
edgeweights4['K', 'D'] = 1
edgeweights4['E', 'L'] = 2
edgeweights4['L', 'E'] = 2
edgeweights4['E', 'M'] = 1
edgeweights4['M', 'E'] = 1
edgeweights4['E', 'N'] = 6
edgeweights4['N', 'E'] = 6
edgeweights4['E', 'O'] = 3
edgeweights4['O', 'E'] = 3
edgeweights4['J', 'P'] = 4
edgeweights4['P', 'J'] = 4
edgeweights4['J', 'Q'] = 5
edgeweights4['Q', 'J'] = 5
edgeweights4['J', 'R'] = 8
edgeweights4['R', 'J'] = 8
edgeweights4['J', 'S'] = 2
edgeweights4['S', 'J'] = 2

pre = {}
post = {}
clock = 1


def longestpath(graph, edgeweights, start_node):
    
    #topologically sort the graph by ordering by decreasing post #s
    dfs(graph, start_node)


    top_sort = []

    for v in post:
        new_entry = (post[v], v)
        heapq.heappush(top_sort, new_entry)
   
    dist_tuple = {}
    prev = {}
    
    while top_sort:
        v = heapq.heappop(top_sort)
        prev[v[1]] = [None, None]
        first_max = 0
        second_max = 0
        #print "v:", v[1]
        if len(graph[v[1]]) == 1:
            dist_tuple[v[1]] = [0, 0]
        
        else:
            list_of_children = list(graph[v[1]])
            
            node_x = list_of_children.pop()
            if dist_tuple.has_key(node_x):
                first_max= max(dist_tuple[node_x][0] + edgeweights[node_x, v[1]], dist_tuple[node_x][1]  + edgeweights[node_x, v[1]])
                prev[v[1]][0] = node_x
           
            node_y = list_of_children.pop()
            if dist_tuple.has_key(node_y):
                second_max = max(dist_tuple[node_y][0] + edgeweights[node_y, v[1]], dist_tuple[node_y][1]  + edgeweights[node_y, v[1]])
                prev[v[1]][1] = node_y   
                        
            while list_of_children:
	        node_z = list_of_children.pop()
                if dist_tuple.has_key(node_z) and post[node_z] < post[v[1]]:
                    if max(dist_tuple[node_z][0], dist_tuple[node_z][1]) + edgeweights[node_z, v[1]] > first_max:
                        first_max = max(dist_tuple[node_z][0], dist_tuple[node_z][1]) + edgeweights[node_z, v[1]]
                        prev[v[1]][0] = node_z

                    elif max(dist_tuple[node_z][0], dist_tuple[node_z][1]) + edgeweights[node_z, v[1]] > second_max:
                        second_max = max(dist_tuple[node_z][0], dist_tuple[node_z][1]) + edgeweights[node_z, v[1]]
                        prev[v[1]][1] = node_z
            if second_max:
                dist_tuple[v[1]] = [first_max, second_max]
            else:
                dist_tuple[v[1]] = [first_max, 0]
    
    for tup in dist_tuple:
        if dist_tuple[tup][0] < dist_tuple[tup][1]:
            dist_tuple[tup][1], dist_tuple[tup][0] = dist_tuple[tup][0], dist_tuple[tup][1]
            prev[tup][1], prev[tup][0] = prev[tup][0], prev[tup][1]

    #print dist_tuple
    max_distance = 0
    for tup in dist_tuple:
        if max_distance < dist_tuple[tup][0] + dist_tuple[tup][1]:
            max_distance = dist_tuple[tup][0] + dist_tuple[tup][1]
            goes_through = tup

    #print "prev", prev
    
    longest_path_rhs = []
    longest_path_lhs = []
    list_to_visit = prev[goes_through]
    
    #visit right hand side
    to_visit = list_to_visit[1]
    while to_visit:
        longest_path_rhs.append(to_visit)
        if prev[to_visit][1] and (edgeweights[to_visit, prev[to_visit][1]]) > (edgeweights [to_visit, prev[to_visit][0]]):
            to_visit = prev[to_visit][1]
        else:
            to_visit = prev[to_visit][0]
 
       
    #visit left hand side
    to_visit = list_to_visit[0]
    while to_visit:
        longest_path_lhs.append(to_visit)
        if prev[to_visit][1] and (edgeweights[to_visit, prev[to_visit][1]]) > (edgeweights [to_visit, prev[to_visit][0]]):
            to_visit = prev[to_visit][1]
        else:
            to_visit = prev[to_visit][0]

    
    longest_path = []
    for node in reversed(longest_path_lhs):
        longest_path.append(node)
    longest_path.append(goes_through)
    for node in longest_path_rhs:
        longest_path.append(node)

 
    return longest_path

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

#print longestpath(graph1, edgeweights1, 'B')
#test case passed

#print longestpath(graph2, edgeweights2, 'A')
#test case passed

#print longestpath(graph2, edgeweights2, 'B')
#test case passed

#print longestpath(graph3, edgeweights3, 'A')
#test case passed

print "The longest path is", longestpath(graph4, edgeweights4, 'A')
