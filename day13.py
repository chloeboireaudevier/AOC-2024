import math
import re
import numpy as np

#file = open("testinput/testinputday13.txt",'r')
file = open("input/inputday13.txt",'r')
content = file.readlines()
file.close()
print(content)

#Get data : arrays -> button A, button B, prize
data = []
for i in range(0,len(content),4):
    machine = []
    for j in range(3):
        if j < 2:
            machine.append([int(s) for s in re.findall(r'\b\d+\b', content[i+j])])
        #PART TWO
        else:
            to_app = [int(s) for s in re.findall(r'\b\d+\b', content[i+j])]
            for k in range (len(to_app)):
                to_app[k] += 10000000000000
            machine.append(to_app)
    data.append(machine)
print(data)

def is_winnable(array):
    buttonA = array[0]
    buttonB = array[1]
    prize = array[2]
    current = (0,0)
    tokens = 0
    mintokens = math.inf
    for i in range(100):
        current = (buttonA[0]*i,buttonA[1]*i)

        for j in range(100):
            current = (buttonA[0]*i+j*buttonB[0],buttonA[1]*i+j*buttonB[1])
            if current[0] == prize[0] and current[1] == prize[1]:
                tokens = i*3 + j
                if tokens < mintokens:
                    mintokens = tokens
                    break
                    #print(i,j)
            elif current[0] > prize[0] or current[1] > prize[1]:
                break
        if mintokens < math.inf:
            break

    return mintokens if mintokens != math.inf else 0

def solve_linear_combination(L1,L2,res):
    x = np.array([[L1[0],L2[0]],
                  [L1[1],L2[1]]])
    
    scalars = np.linalg.solve(x,res) #create solve function with loop to get positive numbers ? + is it fewest ?
    print(scalars)
    print(scalars[1])
    nbA = round(scalars[0])
    nbB = round(scalars[1])

    return nbA, nbB

def is_winnable_part_two(array):
    buttonA = array[0]
    buttonB = array[1]
    prize = array[2]

    nbA,nbB = solve_linear_combination(buttonA,buttonB,prize)

    print(nbA,nbB)

    if 0<=nbA and 0<=nbB and nbA*buttonA[0]+nbB*buttonB[0] == prize[0] and nbA*buttonA[1]+nbB*buttonB[1] == prize[1] :
        nbTokens = 3*nbA + nbB
    else:
        nbTokens = 0
    return nbTokens


def get_prizes(data):
    total_tokens = 0
    for tab in data:
        total_tokens += is_winnable_part_two(tab)
    return total_tokens

#print(is_winnable_part_two(data[0]))
#print(data)
print(get_prizes(data))
#print(solve_linear_combination([17,86],[84,37],[7870,6450]))