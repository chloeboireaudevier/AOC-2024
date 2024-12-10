#file = open("testinput/testinputday10.txt",'r')
file = open("input/inputday10.txt",'r')
content = file.readlines()
file.close()

for i in range(len(content)):
    to_append = list(content[i])
    if i < len(content)-1 :
        to_append.pop(-1)
    content[i] = to_append

def print_tab(data):
    for line in data:
        print(line)

#print(content)
print_tab(content)

def find_starts(data):
    coord_zeros = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '0':
                coord_zeros.append((i,j))
    return coord_zeros

def count_trailhead_score(data,i,j,n,m,nines): #rec ?
    #print(data[i][j])
    if data[i][j] == '9' and (i,j) not in nines:
        nines.append((i,j))
        return 1
    else:
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        count = 0
        for move in moves:
            if 0<=i+move[0]<n and 0<= j+move[1] < m and data[i+move[0]][j+move[1]] == str(int(data[i][j])+1):
                count += count_trailhead_score(data,i+move[0],j+move[1],n,m,nines)
        return count
    
def count_trailhead_score_rating(data,i,j,n,m):
    #print(data[i][j])
    if data[i][j] == '9':
        return 1
    else:
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        count = 0
        for move in moves:
            if 0<=i+move[0]<n and 0<= j+move[1] < m and data[i+move[0]][j+move[1]] == str(int(data[i][j])+1):
                count += count_trailhead_score_rating(data,i+move[0],j+move[1],n,m)
        return count

def get_scores(data):
    scores = []
    coord_zeros = find_starts(data)
    n = len(data)
    m = len(data[0])

    for coord in coord_zeros:
        nines = []
        score = count_trailhead_score(data,coord[0],coord[1],n,m,nines)
        scores.append(score)
    #print(coord_zeros)
    return scores,sum(scores)

def get_scores_rating(data):
    scores = []
    coord_zeros = find_starts(data)
    n = len(data)
    m = len(data[0])

    for coord in coord_zeros:
        score = count_trailhead_score_rating(data,coord[0],coord[1],n,m)
        scores.append(score)
    #print(coord_zeros)
    return scores,sum(scores)

print('Part 1 : ',get_scores(content))
print('Part 2 : ',get_scores_rating(content))