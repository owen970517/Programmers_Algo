def solution(n) :
    answer = 0
    dp = [0] * 100001
    dp[1]=1
    for i in range(2,n+1) :
        dp[i] = ((dp[i-1] * i) + 1)% 1000000007
    answer = dp[n]
    return answer
# def solution(n) :
#     answer = 0
#     dp = [0] * 100001
#     dp[1]=1
#     for i in range(2,n+1) :
#         if i % 2 == 0 :
#             dp[i] = (dp[i-1]*i -1) %1000007
#         else :
#             dp[i] = (dp[i-1]*i +1) %1000007
#     answer = dp[n]
#     return answer
print(solution(4))