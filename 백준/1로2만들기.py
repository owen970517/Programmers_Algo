n = int(input())
dp = [0] * 15
dp[0] = n
print(dp)
cnt = 0
while 1 :
    if dp[cnt] == 1 :
        break
    else :
        if dp[cnt] % 3 == 0 :
            now = dp[cnt]//3
            cnt+=1
            dp[cnt] = now
        if dp[cnt]%2 == 0 :
            now = dp[cnt]//2
            cnt += 1
            dp[cnt] = now
        else :
            now = dp[cnt]- 1
            cnt +=1
            dp[cnt] = now
print(dp) 
print(cnt)