def print_tab(data):
    for line in data:
        print(line)

file = open("testinput/testinputday16.txt",'r')
#file = open("testinput/testinputday16-2.txt",'r')
#file = open("input/inputday16.txt",'r')
content = file.readlines()
file.close()

new_content = []
for i in range(len(content)):
    to_app = list(content[i])
    if i < len(content)-1:
        to_app.pop()
    new_content.append(to_app)

print_tab(new_content)

global directions
directions = [(0,1),(-1,0),(0,-1),(1,0)]

def get_start_end(data):
    start = None
    end = None
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                start = i,j
            elif data[i][j] == 'E':
                end = i,j
    return start,end

def get_paths(data,x,y):
    dir_possible = []
    for dir in directions:
        curr = data[x+dir[0]][y+dir[1]] if 0<=x+dir[0] < len(data) and 0<=y+dir[1]<len(data[0]) else None
        if curr and curr != '#':
            dir_possible.append((x+dir[0],y+dir[1]))
    return dir_possible

def solve(data):
    start,end = get_start_end(data)
    curr = start
    curdir = 0
    path = []
    pile = []
    #path.append(start)
    pile.append(start) #
    while curr != end:              #IDEE NE MARCHE PAS, IL Y A MINIMUM 2 CHOIX SUR UNE LIGEN DROITE
        path.append(curr)
        dir_possible = get_paths(data,curr[0],curr[1])

        while dir_possible == 1:#ligne sans choix
            curr = curr[0]+dir_possible[0][0],curr[1]+dir_possible[0][1]
            path.append(curr)

def shortest_path(graph, node1, node2): #code from https://onestepcode.com/graph-shortest-path-python/
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
    #print(path_index,len(path_list))
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        #print(next_nodes)
        #print(current_path)
        # Search goal node
        if node2 in next_nodes:
            #print("oui")
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

def solve2(data):
    start,end = get_start_end(data)
    graph = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '#':
                dir_possible = get_paths(data,i,j)
                #print(dir_possible)
                graph[(i,j)] = {x for x in dir_possible}
                #print(graph[(i,j)],i,j)
    #print(graph)
    return shortest_path(graph,start,end)

result = solve2(new_content)
print(result)
print(len(result))