n,m,k = map(int,input().split())
li = [0] * n
floor =0
for i in range(m) :
    t,r = map(int,input().split())  
    for j in range(t) :
        li[j] += r
        if li[j] > k :
            floor = j+1
        else :
            break
    if floor > 0 :
        print(i+1,floor)
        break
    print(li)
if floor == 0 :
    print(-1)
