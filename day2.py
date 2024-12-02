def is_safe(array):
    if len(array) == 1 or len(array) == 0:
        return True
    if array[0] == array[1] :
        return False
    increase = (array[1]-array[0]) > 0
    if increase :
        for i in range(0,len(array)-1):
            if array[i+1]<=array[i] or array[i+1]-array[i] >3:
                return False
    else :
        for i in range(0,len(array)-1):
            if array[i+1]>=array[i] or array[i]-array[i+1] >3:
                return False
    return True

def is_safe_damped(array):
    i = 0
    safe = False
    max_i = len(array)
    while safe == False and i < max_i:
        test_array = [data for data in array]
        test_array.pop(i)

        print("array :",array)
        print("test_array :",test_array)
        print('i ',i)
        print('safe : ',safe)

        safe = is_safe(test_array)
        print('safe end loop',safe)
        i+=1
    return safe



f = open('inputday2.txt','r')
content = f.readlines()
print(content)
f.close()

reports = []
for data in content:
    splited = str.split(data)
    reports.append([int(splited_data) for splited_data in splited])

safe_reports = []
for report in reports:
    if is_safe_damped(report):
        safe_reports.append(report)

print("SAFE REPORTS = ",len(safe_reports))


#print(is_safe([7,6,2,1]))
#print(is_safe_damped([9,7,6,2,1]))
#print(reports)