def reFibo(n) :
    if n <= 2 :
        return 1
    else :
        return reFibo(n-1) + reFibo(n-2)
    
def dpFibo(n) :
    dpCnt=0
    for i in range(3,n+1) :
        dp[i] = dp[i-1] + dp[i-2]
        dpCnt += 1
    return dpCnt
n = int(input())

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1

print(reFibo(n),dpFibo(n))