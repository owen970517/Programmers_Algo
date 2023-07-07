n = int(input())
li = []
for _ in range(n) :
    R,G,B = map(int,input().split())
    li.append([R,G,B])
ans = 1e9
for i in range(3) :
    dp = [[1e9,1e9,1e9] for _ in range(n)]
    dp[0][i] = li[0][i]
    for j in range(1, n):
        dp[j][0] = li[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = li[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = li[j][2] + min(dp[j-1][0], dp[j-1][1])
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)