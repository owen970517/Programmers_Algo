import sys

input = sys.stdin.readline

n = int(input())

li = [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = li[0]
dp[2] = li[0] + li[1]
for i in range(3,n+1) :
    dp[i] = max(dp[i-2]+li[i-1],dp[i-3]+li[i-2]+li[i-1],dp[i-1])

print(max(dp))

# stairs = [0] * 301
# for i in range(1, n + 1):
#     stairs[i] = int(input())


# dp = [0] * 301
# dp[1] = stairs[1]
# dp[2] = stairs[1] + stairs[2]
# dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# for i in range(4, n + 1):
#     dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

# print(dp[n])
