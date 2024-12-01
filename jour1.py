def distance(col1,col2):
    tabdist = []
    assert (len(col1)==len(col2))
    for i in range(len(col1)):
        tabdist.append(abs(int(col1[i])-int(col2[i])))
    return tabdist

def sim_score(col1,col2):
    tabscore = []
    similarity_score = 0
    for i in range(len(col1)):
        appear = col2.count(col1[i])
        tabscore.append(col1[i]*appear)
    similarity_score = sum(tabscore)
    return similarity_score

f = open('inputday1.txt','r')
content = f.readlines()
print(content)
f.close()

col1 = []
col2 = []
for data in content:
    c1,c2 = str.split(data)
    col1.append(int(c1))
    col2.append(int(c2))

print(col1,col2)

col1.sort()
col2.sort()

tabdist = distance(col1,col2)

ans = 0

for number in tabdist:
    ans += number

print("ANSWER : ",ans)
print("SIM SCORE = ",sim_score(col1,col2))