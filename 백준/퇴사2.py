n = int(input())
dp=[0] * (n)
li = []
for i in range(n) :
    t,p = map(int,input().split())
    li.append([t,p])
dp[0] = li[0][1]
print(li)
for i in range(n) :
    if i + li[i][0] < n :
        dp[i+li[i][0]] += dp[i]+li[i][1]
print(dp)