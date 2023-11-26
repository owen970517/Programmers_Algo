t = int(input())
dp = [0]* 101
dp[1],dp[2],dp[3] = 1,1,1
for i in range(t) :
    n = int(input())
    for i in range(3,n+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])
# dp =[0] * 1000001
# dp[1] = 1
# dp[2] = 2
# for i in range(3,n+1) :
#     dp[i] = (dp[i-2] + dp[i-1]) % 15746
# print(dp[n])


