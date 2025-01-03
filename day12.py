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

#print_tab(content)

global directions
directions = [(0,1),(-1,0),(0,-1),(1,0)]

def first_occ(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] !='.':
                return data[i][j]
            
def first_occ_index(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] !='.':
                return i,j

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

def get_regions_area(data,n,m,regions):
    area = []
    for region in regions:
        count = 0
        car = first_occ(region)
        for i in range(n):
            for j in range(m):
                if region[i][j] == car:
                    count+=1
        area.append(count)
    return area

def get_regions_permieter(data,n,m,regions):
    perimeter = []
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

def get_regions_side(data,n,m,regions):
    sides = []
    for k in range (len(regions)):
        region = regions[k]
        start = first_occ_index(region)
        single_sides = 0

        cur = start
        curdir = 0
        while not (data[cur[0]+directions[curdir][0]][cur[1]+directions[curdir][1]] !='.' and data[cur[0]+directions[(curdir+1)%4][0]][cur[1]+directions[(curdir+1)%4][1]] == '.'):
            curdir = (curdir+1)%4
        while cur != start:
            
            while data[cur[0]+directions[curdir][0]][cur[1]+directions[curdir][1]] !='.' and data[cur[0]+directions[(curdir+1)%4][0]][cur[1]+directions[(curdir+1)%4][1]] == '.':
                cur = ((cur[0]+directions[curdir][0]),(cur[1]+directions[curdir][1]))
            curdir(curdir+1)%4
            single_sides +=1

        sides.append(single_sides)
    return sides

def count_corners(data,n,m,regions):
    corners = []
    for region in regions:
        #print("------------REG : ",region)
        count = 0
        car = first_occ(region)
        #print("CAR : ",car)
        for i in range(n):
            for j in range(m):
                up = region[i-1][j] if i-1 >= 0 else None
                down = region[i+1][j] if i+1 < n else None
                left = region[i][j-1] if j-1 >= 0 else None
                right = region[i][j+1] if j+1 < m else None
                diag1 = region[i+1][j+1] if j+1 < m and i+1 < n else None
                diag2 = region[i-1][j-1] if i-1 >= 0 and j-1 >=0 else None
                diag3 = region[i+1][j-1] if j-1 >= 0 and i+1 < n else None
                diag4 = region[i-1][j+1] if i-1 >= 0 and j+1 <n else None
                if region[i][j] == car :
                    if (not up or up != car ) and (not right or right!=car):
                        count +=1
                        #print(i,j)
                    if (not up or up != car ) and (not left or left!=car):
                        count +=1
                        #print(i,j)
                    if (not down or down != car ) and (not right or right!=car):
                        count +=1
                        #print(i,j)
                    if (not down or down != car ) and (not left or left!=car):
                        count +=1
                        #print(i,j)
                    if (up and up == car ) and (right and right==car) and diag4!=car:
                        count +=1
                        #print(i,j)
                    if (up and up == car ) and (left and left==car)and diag2!=car:
                        count +=1
                        #print(i,j)
                    if (down and down == car ) and (right and right==car)and diag1!=car:
                        count +=1
                        #print(i,j)
                    if (down and down == car ) and (left and left==car)and diag3!=car:
                        count +=1
                        #print(i,j)
                    #pb quand regions diagonales
                #print(i,j,count)
        corners.append(count)
    return corners

def get_price_fences(data):
    n = len(data)
    m = len(data[0])
    print("before reg")
    regions = get_all_reg(data,n,m)
    print("regions ok")
    area = get_regions_area(data,n,m,regions)
    #perimeter = get_regions_permieter(data,n,m,regions)
    sides = count_corners(data,n,m,regions)
    print("sides ok")
    price = 0
    print(area,sides)
    for i in range(len(area)):
        price += area[i]*sides[i]
    return price
'''
res = get_all_reg(content,len(content),len(content[0]))
for r in res : 
    print('-------------')
    print_tab(r)
print(count_corners(content,len(content),len(content[0]),res))
'''
print(get_price_fences(content))
#print(get_regions_side(content,len(content),len(content[0]),get_all_reg(content,len(content),len(content[0]))))

#print(get_price_fences(content))