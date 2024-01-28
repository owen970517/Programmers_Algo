def quad_tree(x,y,n) :
    global a,b,c
    now = li[x][y]

    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if li[i][j] != now :
                for k in range(3) :
                    for l in range(3) :
                        quad_tree(x+k*n//3,y+l*n//3,n//3)
                return
    if now == -1 :
        a += 1
    elif now == 0 :
        b += 1
    else :
        c += 1

n = int(input())
li = []
a,b,c = 0,0,0

for _ in range(n) :
    s = list(map(int,input().split()))
    li.append(s)

quad_tree(0,0,n)
print(a)
print(b)
print(c)
