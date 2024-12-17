def print_tab(data):
    for line in data:
        print(line)

file = open("testinput/testinputday16.txt",'r')
#file = open("testinput/testinputday16-2.txt",'r')
#file = open("input/inputday16.txt",'r')
content = file.readlines()
file.close()
#print(content)