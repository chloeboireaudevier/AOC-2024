import math

def print_tab(data):
    for line in data:
        print(line)

#file = open("testinputday8.txt",'r')
file = open("inputday8.txt",'r')
content = file.readlines()
file.close()

for i in range(len(content)):
    to_append = list(content[i])
    if i < len(content)-1 :
        to_append.pop(-1)
    content[i] = to_append

#print(content)
print_tab(content)


def get_diff_freq(data):
    freqs = []
    for line in data:
        for car in line:
            if car != '.' and car not in freqs:
                freqs.append(car)
    return freqs

def get_tab_specific_freq(data,freq):
    spec_tab = []
    for line in data:
        if freq in line:
            spec_tab.append(line)
        else :
            spec_tab.append(['.' for i in range(len(line))])
    return spec_tab

def get_specific_frequencies(data):
    freqs = get_diff_freq(data)
    print(freqs)
    numfreqs = len(freqs)
    specific_freq = []
    for i in range(numfreqs):
        specific_freq.append(get_tab_specific_freq(data,freqs[i]))
    return specific_freq,freqs

def get_coord_freq(specific_freq,freq):
    coords = []
    for i in range(len(specific_freq)):
        for j in range(len(specific_freq[0])):
            if specific_freq[i][j] == freq:
                coords.append((i,j))

    return coords

def get_coords_antinodes(tab,coord1,coord2):
    n = len(tab)
    m = len(tab[0])

    coords = []

    distx = abs(coord1[0] - coord2[0])
    disty = abs(coord1[1] - coord2[1])

    if coord1[1] <= coord2[1]:
        first_antinode = (coord1[0]-distx,coord1[1]-disty)
        second_antinode = (coord2[0]+distx,coord2[1]+disty)
    else:
        first_antinode = (coord1[0]-distx,coord1[1]+disty)
        second_antinode = (coord2[0]+distx,coord2[1]-disty)

    if first_antinode[0] < n and first_antinode[0] >= 0 and first_antinode[1] < m and first_antinode[1] >= 0:
        coords.append(first_antinode)
    if second_antinode[0] < n and second_antinode[0] >= 0 and second_antinode[1] < m and second_antinode[1] >= 0:
        coords.append(second_antinode)

    return coords

def get_diagonal_antinodes(tab,coord1,coord2):
    n = len(tab)
    m = len(tab[0])

    coords = []

    diffy = (coord2[1] - coord1[1])

    diffx = (coord2[0] - coord1[0])

    print(diffx,diffy)

    dir = diffy/diffx
    print(dir)

    current = coord1

    if dir > 0 :
        while current[0] >= 0 and current[1] >= 0:
            coords.append(current)
            current = (current[0]-abs(diffx),current[1]-abs(diffy))
        current = coord1
        while current[0] < n and current[1] < m:
            coords.append(current)
            current = (current[0]+abs(diffx),current[1]+abs(diffy))

    else:
        while current[0] >= 0 and current[1] < m:
            coords.append(current)
            current = (current[0]-abs(diffx),current[1]+abs(diffy))
        current = coord1
        while current[0] < n and current[1] >= 0:
            coords.append(current)
            current = (current[0]+abs(diffx),current[1]-abs(diffy))

    return coords

def get_antinodes(specific_freq,freq):
    list_coords = get_coord_freq(specific_freq,freq)

    tab_antinodes = [(['.' for i in range(len(specific_freq[0]))]) for i in range(len(specific_freq))]

    for i in range(len(list_coords)):
        for j in range(i+1,len(list_coords)):
            coords_antinodes = get_coords_antinodes(specific_freq,list_coords[i],list_coords[j])
            coords_antinodes += get_diagonal_antinodes(specific_freq,list_coords[i],list_coords[j])
            for coord in coords_antinodes:
                tab_antinodes[coord[0]][coord[1]] = '#'


    return tab_antinodes

def is_antinode(list_tabs,i,j):
    for tab in list_tabs:
        if tab[i][j] == '#':
            return True
    return False

def merge_tabs(list_tabs):
    merged = [(['.' for i in range(len(list_tabs[0][0]))]) for i in range(len(list_tabs[0]))]

    for i in range(len(merged)):
        for j in range(len(merged[0])):
            if is_antinode(list_tabs,i,j):
                merged[i][j] = '#'
    return merged

def count_occ(data,car):
    occ = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == car:
                occ +=1
    return occ

def get_num_antinodes(content):

    tab_freqs,freqs = get_specific_frequencies(content)

    list_antinodes = []

    for i in range(len(tab_freqs)):
        list_antinodes.append(get_antinodes(tab_freqs[i],freqs[i]))

    merged_antinodes = merge_tabs(list_antinodes)

    print_tab(list_antinodes[0])
    print("------------------")
    print_tab(list_antinodes[1])

    return count_occ(merged_antinodes,'#')

print(get_num_antinodes(content))