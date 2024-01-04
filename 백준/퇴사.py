n = int(input())
dp = [0] * (n+1)
day,price = [],[]
for i in range(n) :
    t,p =map(int,input().split())
    day.append(t)
    price.append(p)

for i in range(n) :
    for j in range(i+day[i],n+1) :
        dp[j] = max(dp[j],dp[i]+price[i])

print(dp[-1])