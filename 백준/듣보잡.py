n,m = map(int,input().split())
dic =dict()
li=[]
for i in range(n+m) :
    s = input()
    if s not in dic :
        dic[s] = 1
    else :
        dic[s] += 1

for i in dic.items() :
    if i[1] == 2 :
        li.append(i[0])
print(len(li))
for i in sorted(li) :
    print(i)

