n = int(input())
li = []
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)

for i in range(n) :
    for j in range(n) :
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
        if j + li[i][j] < n :
            dp[i][j+li[i][j]] += dp[i][j]
        if i + li[i][j] < n :
            dp[i+li[i][j]][j] += dp[i][j]
