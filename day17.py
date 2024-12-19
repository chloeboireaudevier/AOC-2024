import re

#file = open("testinput/testinputday17.txt",'r')
file = open("testinput/testinputday17part2.txt",'r')
#file = open("input/inputday17.txt",'r')
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
    registers_read = data[:index]
    instructions = data[index+1:]
    #print(registers,instructions)

    registers=[]
    for i in range(len(registers_read)):
        registers.append([ int(s) for s in re.findall(r'-?\d+(?:\.\d+)?', registers_read[i])])
        registers[i] = registers[i][0]

    
    instructions = instructions[0].split(',')
    #print(instructions)
    instructions[0] = instructions[0][9:]

    for i in range(len(instructions)):
        instructions[i] = int(instructions[i])

    return registers,instructions

###instructions

def combo_op(registers,operand):
    if 0<= operand <= 3:
        return operand
    elif operand == 4:
        return registers[0]
    elif operand == 5:
        return registers[1]
    elif operand == 6:
        return registers[2]
    else:
        return None

def adv(registers,operand):
    numerator = registers[0]
    denominator = 2**combo_op(registers,operand)
    res = numerator/denominator
    res = int(res)
    registers[0] = res
    return registers

def bxl(registers,operand):
    registers[1] = registers[1] ^ operand
    return registers

def bst(registers,operand):
    registers[1] = (combo_op(registers,operand))%8
    return registers

def jnz(registers,operand,pointer):
    if registers[0] != 0:
        return operand-2
    else :
        return pointer

def bxc(registers,operand):
    registers[1] = registers[1] ^ registers[2]
    return registers

def out(registers, operand):
    return combo_op(registers,operand)%8

def bdv(registers,operand):
    numerator = registers[0]
    denominator = 2**combo_op(registers,operand)
    res = numerator/denominator
    res = int(res)
    registers[1] = res
    return registers

def cdv(registers,operand):
    numerator = registers[0]
    denominator = 2**combo_op(registers,operand)
    res = numerator/denominator
    res = int(res)
    registers[2] = res
    return registers


def run_program(content):
    registers,instructions = get_input(content)
    output = []
    pointer = 0
    while 0<= pointer < len(instructions):
        opcode = instructions[pointer]
        operand = instructions[pointer+1]
        if opcode == 0:
            registers = adv(registers,operand)
        elif opcode == 1:
            registers = bxl(registers,operand)
        elif opcode == 2:
            registers = bst(registers,operand)
        elif opcode == 3:
            pointer = jnz(registers,operand,pointer)
        elif opcode == 4:
            registers = bxc(registers,operand)
        elif opcode == 5:
            output.append(out(registers,operand))
        elif opcode == 6:
            registers = bdv(registers,operand)
        else:
            registers = cdv(registers,operand)
        pointer+=2

    output = ','.join([str(num) for num in output])
    return output

def brute_force_part2(content):
    registers,instructions = get_input(content)
    i = 0
    output = []
    while output != instructions:
        registers[0] = i
        output = []
        pointer = 0
        while 0<= pointer < len(instructions):
            opcode = instructions[pointer]
            operand = instructions[pointer+1]
            if opcode == 0:
                registers = adv(registers,operand)
            elif opcode == 1:
                registers = bxl(registers,operand)
            elif opcode == 2:
                registers = bst(registers,operand)
            elif opcode == 3:
                pointer = jnz(registers,operand,pointer)
            elif opcode == 4:
                registers = bxc(registers,operand)
            elif opcode == 5:
                output.append(out(registers,operand))
            elif opcode == 6:
                registers = bdv(registers,operand)
            else:
                registers = cdv(registers,operand)
            pointer+=2

        output = ','.join([str(num) for num in output])
        print(output)
        i+=1
    return i


print(get_input(content))
print(brute_force_part2(content))