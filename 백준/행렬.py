def list_2d(li) :
    for i in li :
        print(i)

n,m = map(int,input().split())
A,B = [],[]
for i in range(n*2) :
    s = list(input())
    if i<n :
        A.append(s)
    else :
        B.append(s)
print(A)
new=[]
for i in range(n-3) :
    for j in range(m-3) :
        new_li =[row[j:j+3] for row in A[i:i+3]]
        new.append(new_li)
    print(new)
