h,w,x,y = map(int,input().split())
A = [[0] * w for _ in range(h)]
B = []
for i in range(h+x) :
    s = list(map(int,input().split()))
    B.append(s)

for i in range(h) :
    for j in range(w) :
        if i< x or j < y :
            A[i][j] = B[i][j]
        else :
            A[i][j] = B[i][j] - A[i-x][j-y]
for i in A :
    print(*i)
