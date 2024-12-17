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
        if data[x+dir[0]][y+dir[0]] == '.':
            dir_possible.append(dir)
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


