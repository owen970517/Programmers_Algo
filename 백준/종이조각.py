n,m = map(int,input().split())
li = []
ans = 0
for i in range(n) :
    s = list(input())
    li.append(s)

for i in range(n) :
    ans += int(''.join(li[i]))
total = 0
for i in range(m) :
    now = ''
    for j in range(n) :
        now += li[j][i]
    total += int(now)
ans = max(ans,total)
print(ans)