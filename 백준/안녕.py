n=int(input())
hp = list(map(int,input().split()))
happy = list(map(int,input().split()))
hp, happy = [0] + hp, [0] + happy
dp = [[0] * 101 for _ in range(n + 1)]
for i in range(1,n+1) :
    for j in range(1,101) :
        if hp[i] <= j  :
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-hp[i]]+happy[i])
        else :
            dp[i][j] = dp[i-1][j]

print(dp[n][99])