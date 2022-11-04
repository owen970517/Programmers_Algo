def solution(m,n,puddles) :
    answer = 0
    dp = [[0] * (m) for _ in range(n)]
    dp[0][0] = 1
    for i in range(n) :
        for j in range(m) :
            if i ==0 and j ==0 :
                continue
            if [j+1,i+1] in puddles :
                dp[i][j] = 0
            elif i ==0 :
                dp[i][j] = dp[i][j-1]
            elif i != 0 and j == 0 :
                dp[i][j] = dp[i-1][j] 
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[n-1][m-1] % 1000000007
    return answer

print(solution(4,3,[[2,2]]))


# def solution(m,n,puddles) :
#     answer = 0
#     dp = [[0] * (m+1) for _ in range(n+1)]
#     dp[1][1] = 1
#     for i in range(1,n+1) :
#         for j in range(1,m+1) :
#             if i ==1 and j==1 :
#                 continue
#             if [j,i] in puddles :
#                 dp[i][j] = 0
#             else :
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     answer =dp[n][m] % 1000000007
#     return answer