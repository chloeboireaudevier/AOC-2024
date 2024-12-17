import re
import math
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

def init_bots(data):
    robots = []
    for line in data:
        r = Robot((line[0],line[1]),(line[2],line[3]))
        robots.append(r)
    return robots

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
            if grid[i][j] != '.':
                nb_bots += grid[i][j]
    return nb_bots

def move_bots(robots,nbsec):
    for bot in robots:
        bot.move_for_sec(nbsec,grid_height,grid_width)
    return robots

def get_robots_grid(robots):

    final_grid = [['.' for i in range(grid_width)] for i in range(grid_height)]
    #print_tab(final_grid)

    for bot in robots:
        ''' PART ONE
        #bot.move_for_sec(nbsecs,grid_height,grid_width)
        if final_grid[bot.positiony][bot.positionx] != '.':
            final_grid[bot.positiony][bot.positionx] += 1
        else:
            final_grid[bot.positiony][bot.positionx] = 1
        '''
        final_grid[bot.positiony][bot.positionx] = 'X'
    return final_grid

def get_safety_factor(data,nbsecs):
    robots = init_bots(data)
    robots = move_bots(robots,nbsecs)
    final_grid = get_robots_grid(robots)
    quadrants = get_quadrants(final_grid)

    safety_factor = 1
    for q in quadrants:
        #print_tab(q)
        nbBots = get_number_bots(q)
        safety_factor *= nbBots

    #print_tab(final_grid)

    return safety_factor

########################################## Part 2 

def find_easter_egg(data):
    writingFile = open('other/testfile.txt','w')
    robots = init_bots(data)
    for i in range(1,10000,1):
        #print(i)
        robots = move_bots(robots,1)
        final_grid = get_robots_grid(robots)

        str_array = []
        for line in final_grid:
            str_array.append(''.join([str(line[i]) for i in range(len(line))]+['\n']))
        writingFile.write("ITER : "+str(i)+'\n')
        writingFile.writelines(str_array)
        #print(str_array)
        
    writingFile.close()


#print(get_safety_factor(list_data,100))
find_easter_egg(list_data)

'''grid = [[i for i in range(grid_width)] for i in range(grid_height)]
print_tab(grid)
test = get_quadrants(grid)
print(len(test))
for tab in test:
    print('-----------')
    print_tab(tab)

#print(grid[2:][2:])'''