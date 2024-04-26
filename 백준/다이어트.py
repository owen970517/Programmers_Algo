G = int(input())
start,end = 1,2
ans = []

while start < end :
    now = end **2 - start ** 2
    if now == G :
        ans.append(end)
        start += 1
    else :
        if now < G :
            end +=1
        else :
            start += 1
if len(ans)  == 0 :
    print(-1)
else :
    for i in ans :
        print(i)