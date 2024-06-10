n = int(input())
li = list(map(int,input().split()))
ans = []

for i in range(n) :
    if i == 0 :
        now = li[0] // (i+1)
    else :
        now = (li[i] * (i+1)) - sum(ans)
    ans.append(now)
print(*ans)