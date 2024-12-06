#file = open("testinputday6.txt",'r')
file = open("inputday6.txt",'r')
content = file.readlines()
file.close()
print(content)

grid = []
for i in range(len(content)):
    to_append = list(content[i])
    if i != len(content)-1 :
        to_append.pop(-1)
    grid.append(to_append)
    print(to_append)

#print(grid)

def go_to_next_obstacle(grid,x_pos,y_pos,direction):
    x_cur = x_pos
    y_cur = y_pos
    n = len(grid)
    m = len(grid[0])
    while x_cur < n and y_cur < m and grid[x_cur][y_cur] != '#':
        #print('DIRECTIONS ',direction)
        grid[x_cur][y_cur] = 'X'
        x_cur += direction[0]
        y_cur += direction[1]
    return x_cur - direction [0],y_cur - direction[1]

def get_starting_point(data):
    pos = None
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^':
                pos = i,j
    return pos

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def get_path(grid):
    path_grid = grid.copy()
    i_dir = 0
    current = get_starting_point(path_grid)
    n = len(grid)
    m= len(grid[0])
    end = False
    while not end:
        current = go_to_next_obstacle(path_grid,current[0],current[1],directions[i_dir])
        
        if current[0]+directions[i_dir][0] >= n or current[1]+directions[i_dir][1]>= m:
            end = True

        i_dir = (i_dir+1)%4
        #print('CURRENT : ',current)
        current= current[0]+directions[i_dir][0] , current[1]+directions[i_dir][1]
        #print('CURRENT : ',current)

    return path_grid

def count_x(path_grid):
    nb_x = 0
    for i in range(len(path_grid)):
        nb_x += (path_grid[i]).count('X')
    return nb_x


path_grid = get_path(grid)

print(count_x(path_grid))

