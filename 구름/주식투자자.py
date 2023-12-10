import math


n = int(input())
li = []
ans = []
for i in range(n) :
    v,w = input().split()
    v = float(v)
    w = float(w)
    now = v * w
    floor_number = math.floor(now * 10) / 10
    li.append(floor_number)

li = list(enumerate(li))
print(li)
li = sorted(li , key= lambda x :x[1], reverse=True)
print(li)
for i in li :
    ans.append(i[0]+1)
print(ans)