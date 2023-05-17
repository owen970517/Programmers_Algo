t = int(input())
for i in range(t) :
    li = []
    n = int(input())
    for j in range(2) :
        s = list(map(int,input().split()))
        li.append(s)
    for k in range(1,n) :
        if k == 1 :
            li[0][k] += li[1][k-1]
            li[1][k] += li[0][k-1]
        else :
            li[0][k] += max(li[1][k-1],li[1][k-2])
            li[1][k] += max(li[0][k-1],li[0][k-2])
    print(max(max(li[0]),max(li[1])))