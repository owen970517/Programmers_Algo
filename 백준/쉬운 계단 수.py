n = int(input())

dp = [0] * 101

for i in range(1,n+1) :
    dp[i] = (i*9) -1
print(dp[n])