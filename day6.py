#file = open("testinput/testinputday6.txt",'r')
file = open("input/inputday6.txt",'r')
content = file.readlines()
file.close()
print(content)

grid_ = []
for i in range(len(content)):
    to_append = list(content[i])
    if i != len(content)-1 :
        to_append.pop(-1)
    grid_.append(to_append)
    print(to_append)

#print(grid)

def go_to_next_obstacle(grid,x_pos,y_pos,direction):
    x_cur = x_pos
    y_cur = y_pos
    n = len(grid)
    m = len(grid[0])
    while x_cur < n and y_cur < m  and x_cur >= 0 and y_cur >= 0 and grid[x_cur][y_cur] != '#' and grid[x_cur][y_cur] != 'O':
        #print('DIRECTIONS ',direction)
        #print(x_cur,y_cur)
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
    n = len(path_grid)
    m= len(path_grid[0])
    end = False
    while not end:
        current = go_to_next_obstacle(path_grid,current[0],current[1],directions[i_dir])
        
        if current[0]+directions[i_dir][0] >= n or current[0]+directions[i_dir][0] < 0 or current[1]+directions[i_dir][1]>= m or current[1]+directions[i_dir][1]< 0:
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

def get_path_stuck(grid):
    path_grid = grid.copy()
    i_dir = 0
    start = get_starting_point(path_grid)
    current = start
    n = len(path_grid)
    m= len(path_grid[0])
    end = False
    stuck = False
    first = True

    path = [(start,directions[i_dir])]

    while not end:
        current = go_to_next_obstacle(path_grid,current[0],current[1],directions[i_dir])
        if current[0]+directions[i_dir][0] >= n or current[0]+directions[i_dir][0] < 0 or current[1]+directions[i_dir][1]>= m or current[1]+directions[i_dir][1]< 0:
            end = True
            stuck = False
        

        first = False
        i_dir = (i_dir+1)%4
        #print('CURRENT : ',current)
        current= current[0]+directions[i_dir][0] , current[1]+directions[i_dir][1]
        #print('CURRENT : ',current)

        if (current,directions[i_dir]) in path:
            end = True
            stuck = True

        path.append((current,directions[i_dir]))

    return stuck


def get_stuck(grid):
    nb = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #print(nb)
            if grid[i][j] == '.':
                newgrid = [row[:] for row in grid]
                newgrid[i][j] = 'O'
                if get_path_stuck(newgrid):
                    nb+=1
                    #for l in range(len(newgrid)):
                    #    print(newgrid[l])
    return nb



#path_grid = get_path(grid_)
#print(count_x(path_grid))

print(get_stuck(grid_))
