import math
import re

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
        machine.append([int(s) for s in re.findall(r'\b\d+\b', content[i+j])])
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
                    #print(i,j)
            elif current[0] > prize[0] or current[1] > prize[1]:
                break
    return mintokens if mintokens != math.inf else 0


def get_prizes(data):
    total_tokens = 0
    for tab in data:
        total_tokens += is_winnable(tab)
    return total_tokens

#print(is_winnable(data[2]))
#print(data)
print(get_prizes(data))