file = open("testinputday7.txt",'r')
#file = open("inputday7.txt",'r')
content = file.readlines()
file.close()
print(content)

def format(data):
    result = []
    operands = []
    for line in data:
        r,o = line.split(':')

        r = int(r)

        o = o.split(' ')
        o = list(o)

        num_op = []
        for i in range(1,len(o)):
            num_op.append(int(o[i]))

        result.append(r)
        operands.append(num_op)
    return result,operands

#def evaluate(num1,num2,op):
#    if op == '+':
#        return num1 + num2
#    else :
#        return num1*num2

def try_op_rec(res,op):
    if len(op) == 1 and op[0] == res:
        return True
    elif len(op) == 1 and op[0] != res :
        return False
    else:
        return try_op_rec(res, [op[0]+op[1]]+op[2:]) or try_op_rec(res, [op[0]*op[1]]+op[2:])
    
def keep_res_true_eq(list_res, list_op):
    keep = []
    for i in range(len(list_res)):
        if try_op_rec(list_res[i],list_op[i]):
            keep.append(list_res[i])
    return keep

def get_result(content):
    list_results,list_operands = format(content)
    keep = keep_res_true_eq(list_results,list_operands)
    return sum(keep)

print("RES : ",get_result(content))