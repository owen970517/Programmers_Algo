# 조합으로 푸는 방법
def factorial(n) :
    if n <= 1 :
        return 1
    else :
        return n * factorial(n-1)
t = int(input())

for i in range(t) :
    n,m = map(int,input().split())
    now = factorial(m) // (factorial(m-n) * factorial(n))
    print(now)

# dp로 푸는 방법
# dp = [[0] * 30 for _ in range(30)]

# for i in range(30) :    
#     for j in range(30) :
#         if i == 1 :
#             dp[i][j] = j 
#         else :
#             if i == j :
#                 dp[i][j] = 1
#             elif i < j  :
#                 dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

# for i in range(t) :
#     n,m = map(int,input().split())

#     print(dp[n][m])