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

def solve(content,nbbytes):
    data = get_input(content)
    grid = create_grid(data,nbbytes)
    print_tab(grid)
    path = find_path_bfs((0,0),(size-1,size-1),grid)
    return path

#print(get_input(content))
#print_tab(create_grid(get_input(content),nbBytes_test))
path = solve(content,nbBytes_test)
#print(path)
#new_grid = create_grid(get_input(content),nbBytes_test)
print('len',len(path))
'''
for p in path:
    new_grid[p[0]][p[1]] = 'O'
print_tab(new_grid)
'''