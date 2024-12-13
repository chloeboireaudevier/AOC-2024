#file = open("testinput/testinputday12-3.txt",'r')
file = open("input/inputday12.txt",'r')
content = file.readlines()
file.close()
#print(content)

for i in range(len(content)):
    content[i] = list(content[i])
    if i < len(content)-1:
        content[i].pop(-1)

def print_tab(data):
    for line in data:
        print(line)

print_tab(content)

global directions
directions = [(-1,0),(1,0),(0,1),(0,-1)]

def first_occ(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] !='.':
                return data[i][j]

def get_region_from(data,x,y):
    test = [['.' for i in range(len(data[0]))] for i in range(len(data))]
    stack = []
    car = data[x][y]
    stack.append((x,y))
    visited = []
    while stack != []:
        curr = stack.pop()
        test[curr[0]][curr[1]] = car
        visited.append(curr)
        for dir in directions:
            if 0<=curr[0]+dir[0]<len(data) and 0<=curr[1]+dir[1]<len(data[0]) and data[curr[0]+dir[0]][curr[1]+dir[1]] == car and not (curr[0]+dir[0],curr[1]+dir[1]) in visited and not (curr[0]+dir[0],curr[1]+dir[1]) in stack:
                stack.append((curr[0]+dir[0],curr[1]+dir[1]))
    return test


def transform_into_new_regions(data):
    pass





def get_diff_regions(data):
    names=[]
    for line in data:
        for car in line:
            if car not in names:
                names.append(car)
    return names

def get_region_by_name(data,name,n,m):
    region = [['.' for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] == name:
                region[i][j] = name
    return region

def get_regions(data):
    n = len(data)
    m = len(data[0])
    regions = []
    names = get_diff_regions(data)
    for i in range(len(names)):
        regions.append(get_region_by_name(data,names[i],n,m))
    return regions

def get_all_reg(data,n,m):
    regions = []
    for i in range(n):
        for j in range(m):
            reg = get_region_from(data,i,j)
            if not reg in regions:
                regions.append(reg)
    return regions

def get_regions_area_dict(data,n,m):
    area = {}
    for i in range(n):
        for j in range(m):
            if not data[i][j] in area:
                area[data[i][j]] = 1
            else:
                area[data[i][j]] +=1
    return area

def get_regions_area(data,n,m):
    area = []
    regions = get_all_reg(data,n,m)
    for region in regions:
        count = 0
        car = first_occ(region)
        for i in range(n):
            for j in range(m):
                if region[i][j] == car:
                    count+=1
        area.append(count)
    return area

def get_regions_permieter(data,n,m):
    perimeter = []
    regions = get_all_reg(data,n,m)
    for k in range (len(regions)):
        name = first_occ(regions[k])
        region = regions[k]
        single_perim = 0
        for i in range(n):
            for j in range(m):
                if region[i][j] == name:
                    for direction in directions:
                        if i+direction[0] < 0 or i+direction[0] >=n or j+direction[1] < 0 or j+direction[1] >=m or region[i+direction[0]][j+direction[1]] != name:
                            single_perim += 1
        perimeter.append(single_perim)
    return perimeter


def get_price_fences(data):
    n = len(data)
    m = len(data[0])
    area = get_regions_area(data,n,m)
    perimeter = get_regions_permieter(data,n,m)
    price = 0
    print(area,perimeter)
    for i in range(len(perimeter)):
        price += area[i]*perimeter[i]
    return price

print(get_price_fences(content))