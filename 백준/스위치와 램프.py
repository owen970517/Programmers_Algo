from itertools import combinations


n,m = map(int,input().split())
switch = [i for i in range(1,n+1)]
isCan = False
dic = {

}
for i in range(1,n+1) :
    info = list(map(int,input().split()))
    dic[i] = info[1::]

nCr = list(combinations(switch,n-1))
for i in nCr :
    lamp = [False] * (m+1)
    for j in range(n-1) :
        for k in dic[i[j]] :
            if lamp[k] == False :
                lamp[k] = True
    if lamp.count(True) == m :
        isCan = True
        break
if isCan : 
    print(1)
else :
    print(0)
