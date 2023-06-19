n,s,m = map(int,input().split())
v = list(map(int,input().split()))
dp = [0] * (m+1)
dp[0] = s
for i in range(1,n+1) :
    if 0<= dp[i-1]+v[i-1] <= m and 0<= dp[i-1]-v[i-1] <= m:
        dp[i] = max(dp[i-1]+v[i-1], dp[i-1]-v[i-1])
    else :
        if 0<=dp[i-1]+v[i-1]<=m :
            dp[i] = max(dp[i],dp[i-1]+v[i-1])
        if 0<=dp[i-1]-v[i-1]<=m :
            dp[i] = max(dp[i],dp[i-1]-v[i-1])
print(max(dp))