x,y = {},{}
ans = []
for i in range(3) :
    nx,ny = map(int,input().split())
    if nx in x :
        x[nx] += 1
    else :
        x[nx] = 1
    if ny in y :
        y[ny] += 1
    else :
        y[ny] = 1
print(x,y)
for i in x :
    if x[i] < 2 :
        ans.append(i)
for i in y :
    if y[i] < 2 :
        ans.append(i)
print(*ans)