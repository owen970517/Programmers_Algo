def countWays(n):
    MOD = 1000000007
    dp = [0] * (n+2)
    dp[0] = 1

    for i in range(1, n+1):
    
        dp[i] += dp[i-1]
    
        if i >= 3:
            dp[i] += dp[i-3]
    
        dp[i] %= MOD

    return dp[n]
n=int(input())
dp = [0] * (n+2)
dp[0] = 1

for i in range(1, n+1):

    dp[i] += dp[i-1]

    if i >= 3:
        dp[i] += dp[i-3]

    dp[i] %= 1000000007
print(dp[n])

