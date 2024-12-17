def print_tab(data):
    for line in data:
        print(line)

#file = open("testinput/testinputday15part2.txt",'r')
#file = open("testinput/testinputday15-1.txt",'r')
#file = open("testinput/testinputday15-2.txt",'r')
file = open("input/inputday15.txt",'r')
content = file.readlines()
#print(content)

def get_index_separator(data):
    index = 0
    for i in range(len(data)):
        if len(data[i]) == 1:
            index = i
    return index

def get_input(data):
    index = get_index_separator(data)
    box_map = data[:index]
    moves = data[index+1:]

    for i in range(len(box_map)):
        box_map[i] = list(box_map[i])
        box_map[i].pop()

    for i in range(len(moves)):
        if i < len(moves)-1:
            moves[i] = moves[i][:-1]

    moves = ''.join(moves)

    return box_map,moves

def get_index_robot(box_map):
    for i in range(len(box_map)):
        for j in range(len(box_map[0])):
            if box_map[i][j] == '@':
                return i,j
            
def get_direction(dircar):
    direction = (1,0)

    if dircar == '<':
        direction = (0,-1)

    elif dircar =='^':
        direction = (-1,0)

    elif dircar =='>':
        direction = (0,1)

    return direction


def is_movable(box_map,direction,x,y):
    
    next = box_map[x+direction[0]][y+direction[1]]
    if next =='.':
        return True
    elif next =='#':
        return False
    else:
        if next == '[':
            return is_movable(box_map,direction,x+direction[0],y+direction[1]) and is_movable(box_map,direction,x+direction[0],y+direction[1]+1)
        else:
            return is_movable(box_map,direction,x+direction[0],y+direction[1]) and is_movable(box_map,direction,x+direction[0],y+direction[1]-1)

def move_box(box_map,direction,x,y): #part 2
    if box_map[x][y] == '[':
        if is_movable(box_map,direction,x,y) and is_movable(box_map,direction,x,y+1) :
            box_map,index = move(box_map,direction,x,y)
            box_map,index = move(box_map,direction,x,y+1)
        return box_map
    else:
        if is_movable(box_map,direction,x,y) and is_movable(box_map,direction,x,y-1):
            box_map,index = move(box_map,direction,x,y)
            box_map,index = move(box_map,direction,x,y-1)
        return box_map

            
def move(box_map,direction,x,y):#envoyer direction pas dircar
    '''
    print("MOVE")
    print(x,y,direction)
    print('taille tab',len(box_map),len(box_map[0]))
    print_tab(box_map)
    print('ok')'''
    nextcar = box_map[x + direction[0]][y+direction[1]]
    if nextcar == '.':
        box_map[x + direction[0]][y+direction[1]] = box_map[x][y]
        box_map[x][y] = '.'
        return box_map,(x+ direction[0],y+ direction[1])
    elif nextcar == '#':
        return box_map,(x,y)
    else : #nextcar == 'O'
        if direction[0] == 0:
            box_map,index = move(box_map,direction,x+direction[0],y+direction[1])
            nextcar = box_map[x + direction[0]][y+direction[1]]
            if nextcar == '.':
                box_map[x + direction[0]][y+direction[1]] = box_map[x][y]
                box_map[x][y] = '.'
                return box_map,(x+ direction[0],y+ direction[1])
            else:
                return box_map,(x,y)
        else: #case move up or down -> whole boxes to check
            box_map = move_box(box_map,direction,x+direction[0],y+direction[1])
            nextcar = box_map[x + direction[0]][y+direction[1]]
            if nextcar == '.':
                box_map[x + direction[0]][y+direction[1]] = box_map[x][y]
                box_map[x][y] = '.'
                return box_map,(x+ direction[0],y+ direction[1])
            else:
                return box_map,(x,y)

def get_GPS_box(xbox, ybox):
    return 100*xbox + ybox

def get_sum_GPS(data):
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '[': #part one : O part two : [
                sum += get_GPS_box(i,j)
    return sum

###### PART 2

def scale_map(box_map):
    n = len(box_map)
    m = len(box_map[0])
    #new_map = [['.' for i in range(m*2)] for j in range(n)]
    new_map = []
    for i in range(n):
        line = []
        for j in range(m):
            current =  box_map[i][j]
            if current == 'O':
                line.append('[')
                line.append(']')
            elif current == '@':
                line.append('@')
                line.append('.')
            else:
                line.append(current)
                line.append(current)
        new_map.append(line)
    return new_map

def solve(content):
    box_map, moves = get_input(content)
    scaled = scale_map(box_map)
    indexRob = get_index_robot(scaled)
    print("init")
    print_tab(scaled)
    for dir in moves:
        scaled,indexRob = move(scaled,get_direction(dir),indexRob[0],indexRob[1])
        #print(indexRob == get_index_robot(box_map))
        '''
        print('----------')
        print("direction : ",dir)
        print_tab(scaled)'''

    return get_sum_GPS(scaled)


#print_tab(scale_map(get_input(content)[0]))
print(solve(content))

###### SOLVE

#print(solve(content))
#print(get_input(content))

'''
input = (get_input(content))
#rob = get_index_robot(input[0])
for i in range(len(input[1])):
    print("---------------------")
    print(i)
    print_tab(move(input[0],get_direction(input[1][i]),get_index_robot(input[0])[0],get_index_robot(input[0])[1]))
'''