n = int(input())
li = list(input())
dp = [1e9] * (n+1)
dp[0] = 0
for i in range(1,n) :
    for j in range(i) :
        if li[i] == 'O' and li[j] == 'B' :
            dp[i] = min(dp[i],dp[j]+pow(i-j,2))
        elif li[i] == 'J' and li[j] =='O' :
            dp[i] = min(dp[i],dp[j]+pow(i-j,2))
        elif li[i] == 'B' and li[j] == 'J' :
            dp[i] = min(dp[i],dp[j]+pow(i-j,2))
print(dp)
if dp[n-1] != 1e9 :
    print(dp[n-1])
else :
    print(-1)