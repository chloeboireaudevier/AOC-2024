import re

#DATA
#file = open("testinput/testinputday14.txt",'r')
file = open("input/inputday14.txt",'r')
content = file.readlines()
file.close()
#print(content)

#GRID CHARACTERISTICS
global grid_height
global grid_width
grid_width = 101
grid_height = 103

def print_tab(data):
    for line in data:
        print(line)

list_data = []
for line in content:
    list_data.append([int(s) for s in re.findall(r'-?\d+(?:\.\d+)?', line)]) #Get every number from the string, handles negative numbers
#print(list_data)

class Robot:
    def __init__(self,position,velocity):
        self.positionx = position[0]
        self.positiony = position[1]
        self.velocityx = velocity[0]
        self.velocityy = velocity[1]

    def move(self,n,m):
        if self.velocityx >= 0:
            for i in range(self.velocityx):
                self.positionx +=1
                if self.positionx>= m:
                    self.positionx = 0
        else :
            for i in range(abs(self.velocityx)):
                self.positionx -=1
                if self.positionx < 0:
                    self.positionx = m-1

        if self.velocityy >= 0:
            for i in range(self.velocityy):
                self.positiony +=1
                if self.positiony>= n:
                    self.positiony = 0
        else :
            for i in range(abs(self.velocityy)):
                self.positiony -=1
                if self.positiony < 0:
                    self.positiony = n-1


    def move_for_sec(self, nbSec,n,m):
        for i in range(nbSec):
            self.move(n,m)
            #print(self.positionx,self.positiony)

#r = Robot((2,4),(2,-3))
#r.move_for_sec(5,7,11)

def get_quadrants(tab):
    height_split = grid_height//2
    width_split = grid_width//2
    quadrants = []
    quadrants.append([tab[i][:width_split] for i in range(height_split)])
    quadrants.append([tab[i][width_split+1:] for i in range(height_split)])
    quadrants.append([tab[i][:width_split] for i in range(height_split+1,grid_height)])
    quadrants.append([tab[i][width_split+1:] for i in range(height_split+1,grid_height)])
    return quadrants

def get_number_bots(grid):
    nb_bots = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            nb_bots += grid[i][j]
    return nb_bots

def get_robots_grid(data):
    robots = []
    for line in data:
        r = Robot((line[0],line[1]),(line[2],line[3]))
        robots.append(r)

    final_grid = [[0 for i in range(grid_width)] for i in range(grid_height)]
    #print_tab(final_grid)

    for bot in robots:
        bot.move_for_sec(100,grid_height,grid_width)
        final_grid[bot.positiony][bot.positionx] += 1

    quadrants = get_quadrants(final_grid)

    safety_factor = 1
    for q in quadrants:
        #print_tab(q)
        safety_factor *= get_number_bots(q)

    #print_tab(final_grid)

    return safety_factor

print(get_robots_grid(list_data))

'''grid = [[i for i in range(grid_width)] for i in range(grid_height)]
print_tab(grid)
test = get_quadrants(grid)
print(len(test))
for tab in test:
    print('-----------')
    print_tab(tab)

#print(grid[2:][2:])'''