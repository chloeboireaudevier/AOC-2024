def is_safe(array):
    if len(array) == 1 :
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

def is_safe_damped(array): #modify code so it re-does the pb (careful if recusive)
    if len(array) == 1 :
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
    if is_safe(report):
        safe_reports.append(report)

print("SAFE REPORTS = ",len(safe_reports))


print(is_safe([1,3,2,4,5]))
#print(reports)