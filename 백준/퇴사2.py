# n = int(input())
# dp=[0] * (n+1)
# li = []
# for i in range(n) :
#     t,p = map(int,input().split())
#     li.append([t,p])

# for i in range(1, n + 1):
#     dp[i] = max(dp[i],dp[i-1])
#     if i + li[i-1][0] - 1  <= n: 
#         dp[i + li[i-1][0] - 1 ] = max(dp[i + li[i-1][0] - 1 ], dp[i - 1] + li[i-1][1])
# print(max(dp))

from sys import stdin

N = int(stdin.readline())
dp = [0]*(N+1)
for i in range(1, N+1):
    t, p = map(int, stdin.readline().split())
    dp[i] = max(dp[i-1], dp[i])
    if i+t-1<=N:
        dp[i+t-1] = max(dp[i-1]+p, dp[i+t-1])
print(max(dp))