#parse text, put in array any 12-lengthed str starting with m
#create is_valid function
#create multiply(str) function
#get the sum
import re

def is_valid_num(data):
    if data[:4]!='mul(':
        return False,None

    i= 5
    while i < len(data) and data[i] != ')':
        i+=1
    if i >= len(data):
        return False,None
    data = data[:i+1]

    #print("DATA ::",data)
    
    if len(data) < 8:
        return False,None

    data_to_split = data[4:len(data)-1]
    #print("data_to_s is valid ",data_to_split)
    if data_to_split[0] ==',' or data_to_split[-1]==',' or (',' not in data_to_split):
        return False,None
    #print("PASSED")
    first_op,second_op = data_to_split.split(',')

    #print("data is valid ",data)
    #print("end valid : ",(first_op.isdigit() and second_op.isdigit()),data)
    return ((first_op.isdigit() and second_op.isdigit()),data)

def multiplication(data):
    #print("data mul ",data)
    operands = data[4:len(data)-1]
    #print("operands mul ",operands)
    first_op,second_op = operands.split(',')
    return int(first_op) * int(second_op)
 
# Start of code
file = open("input/inputday3.txt",'r')
content = file.read()
file.close()
print(content)


possible_mul = []
i = 0
while i<len(content):
    if content[i] == 'm':
        possible_mul.append(content[i:i+12])
    elif content[i:i+7]=="don't()":
        while content[i:i+4]!="do()" and i<len(content):
            i+=1
    i+=1

print(possible_mul)

valid_mul = []
for i in range(len(possible_mul)):
    #print(is_valid_num(possible_mul[i])[0])
    if is_valid_num(possible_mul[i])[0]:
        #print((possible_mul[i])[1])
        valid_mul.append(is_valid_num(possible_mul[i])[1])

print("VALID MUL :",valid_mul)

sum = 0
for i in range(len(valid_mul)):
    if is_valid_num(valid_mul[i]):
        sum += multiplication(valid_mul[i])

print(sum)
#print(multiplication("mul(3,2)"))
