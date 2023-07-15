def solution(n,money) :
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1

    for i in money :
        for j in range(i,n+1) :
            if j>= i :
                dp[j] += dp[j-i]

    return answer

print(solution(5,[1,2,5]))