#file = open("testinputday9.txt",'r')
file = open("inputday9.txt",'r')
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

def move_blocks(data):
    end_index = len(data)-1
    num_disk = get_number_disk(data)
    for i in range(num_disk):
        if data[i] == '.':
            replace = data[end_index]
            while replace == '.':
                end_index -=1
                replace = data[end_index]
            data[i] = replace
            data[end_index] = '.'
    return data[:num_disk]

def get_checksum(ordered_data):
    sum = 0
    for i in range(len(ordered_data)):
        sum += i*int(ordered_data[i])
    return sum

formatted = format_disk(content)
print(formatted)
ordered = move_blocks(formatted)
print(ordered)
print(get_checksum(ordered))