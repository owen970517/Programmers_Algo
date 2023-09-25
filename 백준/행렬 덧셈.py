n,m = map(int,input().split())
A,B = [],[]
for _ in range(n) :
    li = list(map(int,input().split()))
    A.append(li)
for _ in range(m) :
    li = list(map(int,input().split()))
    B.append(li)
for i in range(n) :
    for j in range(m) :
        k = A[i][j] + B[i][j]
        print(k,end=' ')
    print()