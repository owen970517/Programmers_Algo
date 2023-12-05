from itertools import product


n = int(input())
dp = [0] * 31
for i in range(1,n+1) :
    now = 3 ** i 
    dp[i] = dp[i-1] + now
print(dp[n])