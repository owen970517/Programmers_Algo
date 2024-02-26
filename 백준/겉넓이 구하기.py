n,m = map(int,input().split())

li = []
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
ans = 0
up = n*m
a,b = 0,0

for i in range(n) :
    for j in range(m) :
        if j == 0 :
            a += li[i][j]
        else :
            if li[i][j-1] < li[i][j] :
                a += (li[i][j] - li[i][j-1])

for i in range(m) :
    for j in range(n) :
        if j == 0 :
            b += li[j][i]
        else :
            if li[j-1][i] < li[j][i] :
                b += (li[j][i] - li[j-1][i])     

ans = 2 * (up+a+b)
print(ans)