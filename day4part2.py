#file = open("testinputday4.txt",'r')
file = open("inputday4.txt",'r')
content = file.readlines()
file.close()
print(content)

def search_x_mas(data,x_index,y_index,x_dir,y_dir): #on compte chaque x deux fois puis divise total par 2
    searched = ['M','A','S']
    i_searched = 0

    n = len(data)
    m = len(data[-1])

    found = False
    possible = True

    x_cursor, y_cursor = x_index + x_dir, y_index + y_dir
    while possible and not found:
        if x_cursor >= n or x_cursor < 0 or y_cursor >= m or y_cursor < 0:
            possible = False
        else:
            if data[x_cursor][y_cursor] == searched[i_searched]:
                #print("found a letter : ",searched[i_searched])
                i_searched +=1
                #print("i searched :",i_searched)
                if i_searched >=len(searched):
                    #print("TRUE")
                    found = True
            else:
                possible = False
        x_cursor, y_cursor = x_cursor + x_dir, y_cursor + y_dir
    return found

words = 0
for i in range(len(content)):
    for j in range(len(content[-1])):
        if content[i][j] == 'X':
            for k in range(-1,2):
                for l in range(-1,2):
                    if search_x_mas(content,i,j,k,l):
                        #word_found = content[i][j]+content[i+k][j+l]+content[i+k+k][j+l+l]+content[i+k+k+k][j+l+l+l]
                        #if word_found !='XMAS':
                        #    print(word_found)
                        words +=1

print(words)
