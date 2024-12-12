#file = open("testinput/testinputday11.txt",'r')
file = open("input/inputday11.txt",'r')
content = file.read()
file.close()

content = content.split(' ')
content[-1] = content[-1][:-1]
#for i in range(len(content)):
    #content[i] = int(content[i])
print(content)

def get_length(num):
    if num == 0:
        return 0
    else:
        return 1 + get_length(num//10)

def split_num(num):
    num = str(num)
    split = len(num)//2
    left = num[:split]
    right = num[split:]
    return int(left),int(right)

def blink(data):
    new_data = []
    for i in range(len(data)):
        if data[i] == 0:
            new_data.append(1)
        elif (get_length(data[i]))%2 == 0:
            left_half,right_half = split_num(data[i])
            new_data.append(left_half)
            new_data.append(right_half)
        else:
            new_data.append(2024*data[i])
    return new_data

def blink_v2(data,numblinks):
    new_data = []
    for i in range(len(data)):
        pile = []
        pile.append(data[i])
        i = 0
        while pile!=[]:
            print(pile)
            current = pile.pop()
            split = False
            for j in range(numblinks-i):
                if current == 0:
                    current = 1
                elif (get_length(current))%2 == 0:
                    left_half,right_half = split_num(current)
                    pile.append(right_half)
                    pile.append(left_half)
                    split = True
                else:
                    current = 2024*current

            if not split:
                new_data.append(current)
            i+=1
    return new_data
        
def blink_rec(data,numblink):
    if data == [] or numblink <= 0:
        return data
    else:
        if data[0] == 0:
            return blink_rec([1] ,numblink-1)+ blink_rec(data[1:],numblink)
        elif get_length(data[0])%2 == 0:
            left,right = split_num(data[0])
            return blink_rec([left],numblink-1)+blink_rec([right],numblink-1)+blink_rec(data[1:],numblink)
        else:
            data[0] = 2024*data[0]
            return blink_rec([data[0]],numblink-1)+blink_rec(data[1:],numblink)
        
def count_stones(stone,numblink,dico = {}): #CODE Mr RIO : Idee -> mettre le nombre de stones crees par un etat (on ne veut pas l'etat final, juste le nombre de stones)
    key = stone,numblink
    if key in dico:
        return dico[key]
    if numblink == 0:
        res = 1
    elif stone == '0':
        res = count_stones('1',numblink-1,dico)
    elif len(stone)%2 == 0:
        left,right = split_num(int(stone))
        res = count_stones(str(left),numblink-1,dico)+count_stones(str(right),numblink-1,dico)
    else:
        res = count_stones(str(int(stone)*2024),numblink-1)
    dico[key] = res
    return res


#for i in range(75):
#    print(i)
#    content = blink(content)
print(len(content))
count = 0
for stone in content:
    count += count_stones(stone,75)
print(count)
#print(len(blink_rec(content,75)))