n = int(input())
dp = [0] * 101

for i in range(1,8) :
    dp[i] = i

for i in range(1,n+1) :
    for j in range(3,n+1) :
        if i-j < 0 :
            break
        dp[i] = max(dp[i], dp[i-j] *(j-1))

print(dp[n])