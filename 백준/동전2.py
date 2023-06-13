n,k = map(int,input().split())
coin = []
dp = [10001] * (k+1)
dp[0] = 0
for i in range(n) :
    s = int(input())
    coin.append(s)

for i in coin :
    for j in range(i,k+1) :
        dp[j] = min(dp[j] , dp[j-i]+1)

if dp[k] == 10001 :
    print(-1)
else :
    print(dp[k])
