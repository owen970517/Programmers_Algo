n = int(input())
li = list(map(int,input().split()))
ans = max(li)
now = li[0]
for i in range(1,n) :
    if li[i] - li[i-1] == 1 :    
        now += li[i]
    else :
        now = 0
        now+=li[i]
    ans = max(ans,now)
print(ans)