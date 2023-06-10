n,m = map(int,input().split())
li = list(map(int,input().split()))
interval_sum = li[0]
start,end = 0,0
ans = 1e9
while 1 :
    if interval_sum >= m :
        interval_sum -= li[start]
        ans = min(ans, end-start+1)
        start += 1
    else :
        end += 1
        if end == n :
            break
        interval_sum += li[end]
if ans == 1e9 :
    print(0)
else :
    print(ans)

