n,k = map(int,input().split())
A = list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
print(A,B)
n= 0
while 1 :
    if n == k :
        break
    A[n],B[n] = B[n],A[n]
    n+=1
print(A)
print(sum(A)) 