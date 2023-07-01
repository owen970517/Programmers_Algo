n,m = map(int,input().split())
w = []
for i in range(n) :
    s = list(input())
    w.append(s)
for i in range(n) :
    for j in range(m) :
        if w[i][j] == 'c' :
            w[i][j] = 0
        if w[i][j]=='.' :
            if j==0 or w[i][j-1] == -1:
                w[i][j] = -1
            else :
                w[i][j] = w[i][j-1]+1
for i in w :
    print(*i)
