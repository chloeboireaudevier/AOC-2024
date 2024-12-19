def print_tab(data):
    for line in data:
        print(line)

#file = open("testinput/testinputday19.txt",'r')
file = open("input/inputday19.txt",'r')
content = file.readlines()
file.close()

print(content)

def get_index_separator(data):
    index = 0
    for i in range(len(data)):
        if len(data[i]) == 1:
            index = i
    return index

def get_input(data):
    index = get_index_separator(data)
    designs = data[:index]
    patterns = data[index+1:]
    print(designs)

    designs = designs[0].split(',')
    designs[-1] = designs[-1][:-1]

    for i in range(len(designs)):
        designs[i] = designs[i].strip()
    designs.sort(key=len)

    for i in range(len(patterns)):
        if i < len(patterns)-1:
            patterns[i] = patterns[i][:-1]

    return designs,patterns

def starts_with(pattern,design):
    starts = True
    i = 0
    while starts and i < len(pattern):
        if i >= len(design) or pattern[i] != design[i]:
            starts = False
        i+=1
    return starts


def get_possible_patterns(patterns,design):
    poss = []
    for p in patterns:
        if starts_with(p,design):
            poss.append(design[len(p):])
    return poss

def is_possible(patterns,design):
    if design =='':
        return True
    else: #case false traité à l'intérieur ?
        possible_des = get_possible_patterns(patterns,design)
        res = False
        for p in possible_des:
            res = res or is_possible(patterns,p)
        return res

def solve(content):
    patterns,designs = get_input(content)
    nbPossible = 0
    for d in designs:
        if is_possible(patterns,d):
            nbPossible +=1
    return nbPossible


print(get_input(content))
print(solve(content))
