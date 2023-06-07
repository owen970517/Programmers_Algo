def solution(money) :
    answer = 0
    dp = [0] * 1001
    for i in range(1,len(money)+1) :
        if i+1 > len(money) and i+2 > len(money) :
            dp[i] = max(money[i-1]+money[abs(len(money)-(i+1))-1],money[i-1]+money[abs(len(money)-(i+2))-1])
        if i+1 < len(money) and i+2 < len(money):
            dp[i] = max(money[i-1]+money[i+1] , money[i-1]+money[i+2])
    print(max(dp))
    return answer

print(solution([1,2,3,1]))