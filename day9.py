#file = open("testinput/testinputday9.txt",'r')
file = open("input/inputday9.txt",'r')
content = file.read()
file.close()

content = content.replace('\n','')

print(content)

def format_disk(line):
    data = []
    file_id = 0
    for i in range(len(line)):
        if i%2 == 0:
            for j in range(int(line[i])):
                data.append(str(file_id))
            file_id+=1
        else :
            for j in range(int(line[i])):
                data.append('.')
    return data

def get_number_disk(data):
    count = 0
    for i in range(len(data)):
        if data[i].isdigit():
            count +=1
    return count

def get_size_same_car_front(data,index):
    size = 1
    while index+size < len(data) and data[index+size] == data[index]:
        size+=1
    return size

def get_size_same_car_back(data,index):
    size = 1
    while index-size >=0 and data[index-size] == data[index]:
        size+=1
    return size

def move_blocks(data):
    end_index = len(data)-1
    #num_disk = get_number_disk(data)
    index_blank = 0
    i=int(data[-1])

    while 0<=i :
        print(i)
        index_blank = 0

        fit = False

        while data[end_index]!= str(i):
            end_index-=1

        size_num = get_size_same_car_back(data,end_index)

        while not fit and index_blank < end_index:
            #print(i)
            while index_blank < end_index and data[index_blank]!= '.':
                #print(index_blank,i)
                index_blank+=1

            size_blank = get_size_same_car_front(data,index_blank)

            if data[index_blank] == '.' and size_blank>=size_num and index_blank < end_index:
                fit = True
            else:
                index_blank +=  size_blank

        #print('index blank',index_blank,'end',end_index)
        #print(fit)
        if fit :
            while data[end_index] == str(i) and end_index > index_blank:
                #print('loop')
                data[end_index] = '.'
                data[index_blank] = str(i)
                end_index-=1
                index_blank +=1
                #print('data',data)
                #print(end_index > size_blank)

        i-=1

    return data


def get_checksum(ordered_data):
    sum = 0
    for i in range(len(ordered_data)):
        if ordered_data[i]!='.':
            sum += i*int(ordered_data[i])
    return sum

formatted = format_disk(content)
print(formatted)
ordered = move_blocks(formatted)
print(ordered)
print(get_checksum(ordered))
#print(len(content)//2)