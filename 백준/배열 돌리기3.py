n,m,r = map(int,input().split())

li = []
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
op = list(map(int,input().split()))

for i in op :
    if i == 1 :
        li = li[::-1]
    elif i == 2 :
        now = []
        for i in li :
            now.append(i[::-1])
        li = now
    elif i == 3 :
        now = [[0] * n for _ in range(m)]
        for i in range(m) :
            for j in range(n) :
                now[i][j]= li[n-j-1][i]
        li = now
        n,m=m,n
    elif i == 4 :
        now = [[0] * n for _ in range(m)]
        for i in range(m) :
            for j in range(n) :
                now[i][j] = li[j][m-i-1]
        li = now
        n,m = m,n
    elif i == 5 :
        now = [[0] * m for _ in range(n)]
        for i in range(n//2) :
            for j in range(m//2) :
                now[i][j + m//2] = li[i][j]
        
        for i in range(n//2) :
            for j in range(m//2,m) :
                now[i+n//2][j] = li[i][j]

        for i in range(n//2,n) :
            for j in range(m//2,m) :
                now[i][j-m//2] = li[i][j]
        
        for i in range(n//2,n) :
            for j in range(m//2) :
                now[i-n//2][j] = li[i][j]
        li = now

    elif i == 6 :
        now = [[0] * m for _ in range(n)]
        for i in range(n//2) :
            for j in range(m//2) :
                now[i+n//2][j] = li[i][j]
        
        for i in range(n//2) :
            for j in range(m//2,m) :
                now[i][j-m//2] = li[i][j]

        for i in range(n//2,n) :
            for j in range(m//2,m) :
                now[i-n//2][j] = li[i][j]

        for i in range(n//2,n) :
            for j in range(m//2) :
                now[i][j+m//2] = li[i][j]
        li = now
for i in li :
    print(*i)