import numpy as np

x = np.array([[94,22], #EN COLONNE
             [34,67]])
y = ([8400,5400])
scalars = np.linalg.solve(x,y)
print(scalars)

array = [[94,34],[22,67]]

x2 = np.array(array)
y2 = ([8400,5400])
print(np.linalg.solve(x2,y2))

print(68.32//10)

l = ['i','l','o','v']
print(''.join(l))

print(len('\n'))

designs ='a,b,c'
designs = designs.split(',')
print(designs)
print(designs[1:])