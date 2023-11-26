n = int(input())
li =list(map(int,input().split()))
re_li = li[::-1]

dp = [1] * n 
Rdp = [1] * n

for i in range(n) :
    for j in range(i) :
        if li[i] > li[j] :
            dp[i] = max(dp[i] , dp[j]+1)

for i in range(n) :
    for j in range(i) :
        if re_li[i] > re_li[j] :
            Rdp[i] = max(Rdp[i] , Rdp[j]+1)

Rdp = Rdp[::-1]
for i in range(n) :
    dp[i]=dp[i]+Rdp[i]

print(max(dp)-1)