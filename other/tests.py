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
h = [1,2,3]
print(','.join([str(j) for j in h]))

print(not False and True)
a = None
if a :
    print("hello")

g = {}
l = [(1,2),(3,4)]
g['a'] = { x for x in l}
print(g['a'])

print([1,2,3][:0])