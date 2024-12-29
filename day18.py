import re

def print_tab(data):
    for line in data:
        print(line)


#file = open("testinput/testinputday18.txt",'r')
file = open("input/inputday18.txt",'r')
content = file.readlines()
file.close()
print(content)

global size
size = 71

global nbBytes_test
nbBytes_test = 1024

def get_input(data):
    new_data=[]
    for i in range(len(data)):
        new_data.append([ int(s) for s in re.findall(r'-?\d+(?:\.\d+)?', data[i])])
    return new_data

def create_grid(data,nbbytes):
    grid = [['.' for j in range(size)] for i in range(size)]
    for coord in data[:nbbytes]:
        #print(coord)
        grid[coord[1]][coord[0]] = '#'
    return grid

# functions for the so function
global directions
directions = [(0,1),(-1,0),(0,-1),(1,0)]

def get_neighbors(node,grid):
    neighbors = []
    for d in directions:
        next = node[0] + d[0],node[1]+d[1]
        if 0<= next[0] < size and 0<=next[1]<size and grid[next[0]][next[1]] =='.':
            neighbors.append(next)
    return neighbors


#code from stackoverflow

def find_path_bfs(s, e, grid):
    queue = [(s, [])]  # start point, empty path
    visited = []

    while len(queue) > 0:
        #print('searching')
        node, path = queue.pop(0)
        path.append(node)
        visited.append(node)
        grid[node[0]][node[1]] = 'O'

        if node == e:
            return path

        adj_nodes = get_neighbors(node, grid)
        for item in adj_nodes:
            if not item in visited:
                queue.append((item, path[:]))
    return None

def get_paths(data,x,y):
    dir_possible = []
    for dir in directions:
        curr = data[x+dir[0]][y+dir[1]] if 0<=x+dir[0] < len(data) and 0<=y+dir[1]<len(data[0]) else None
        if curr and curr != '#':
            dir_possible.append((x+dir[0],y+dir[1]))
    return dir_possible

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



def solve(content,nbbytes):
    data = get_input(content)
    grid = create_grid(data,nbbytes)
    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '#':
                dir_possible = get_paths(grid,i,j)
                #print(dir_possible)
                graph[(i,j)] = {x for x in dir_possible}
                #print(graph[(i,j)],i,j)
    return shortest_path(graph,(0,0),(size-1,size-1))

def solvepart2(content):
    data = get_input(content)
    nbbytes = 0
    grid = create_grid(data,nbbytes)
    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '#':
                dir_possible = get_paths(grid,i,j)
                #print(dir_possible)
                graph[(i,j)] = {x for x in dir_possible}
                #print(graph[(i,j)],i,j)
    shortest = shortest_path(graph,(0,0),(size-1,size-1))
    while shortest !=[] and nbbytes < len(data):
        nbbytes+=1
        grid = create_grid(data,nbbytes)
        graph = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '#':
                    dir_possible = get_paths(grid,i,j)
                    #print(dir_possible)
                    graph[(i,j)] = {x for x in dir_possible}
                    #print(graph[(i,j)],i,j)
        shortest = shortest_path(graph,(0,0),(size-1,size-1))
    return data[nbbytes-1],0<=nbbytes< len(data)

#print(get_input(content))
#print_tab(create_grid(get_input(content),nbBytes_test))
#path = solve(content,nbBytes_test)
#print(path)
#new_grid = create_grid(get_input(content),nbBytes_test)
#print(path)
#print('len',len(path))
'''
for p in path:
    new_grid[p[0]][p[1]] = 'O'
print_tab(new_grid)
'''
print(solvepart2(content))