n,m = map(int,input().split())
A,B = [],[]
for i in range(n*2) :
    s = list(map(int,input()))
    if i<n :
        A.append(s)
    else :
        B.append(s)
cnt = 0
for i in range(n-2) :
    for j in range(m-2) :
        if A[i][j] != B[i][j] :
            for k in range(i,i+3) :
                for l in range(j,j+3) :
                    A[k][l] = 1-A[k][l]
            cnt += 1
if A == B :
    print(cnt)
else :
    print(-1)
