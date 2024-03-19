n,m = map(int,input().split())
A = []
for i in range(n) :
    s = list(map(int,input().split()))
    A.append(s)
m,k = map(int,input().split())
B = []
for i in range(m) :
    s = list(map(int,input().split()))
    B.append(s)
res = [[0] * k for _ in range(n)]
for i in range(n) :
    for j in range(k) :
        for l in range(m) :
            res[i][j] += A[i][l] * B[l][j]

for i in res :
    print(*i)
