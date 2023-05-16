n,m = map(int,input().split())
w = []
for i in range(n) :
    s = list(input())
    w.append(s)
print(w)
for i in range(n) :
    for j in range(m) :
        if w[i][j] == 'c' :
            w[i][j] = 0
        if w[i][j]=='.' :
            w[i][j] = w[i][j-1] + 1
print(w)