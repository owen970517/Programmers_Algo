# 냅색 알고리즘 (DP) 담을수 있는 무게의 최댓값이 정해져 있고, 일정 가치와 무게를 가진 짐들을 골라 가치의 합이 최대가 되도록 할 때 사용
n,k = map(int,input().split())
backpack = [[0,0]]
dp =[[0]*(k+1) for _ in range(n+1)]
for i in range(n) : 
    w,v = map(int,input().split())
    backpack.append([w,v])

for i in range(1,n+1) :
    for j in range(1,k+1) :
        w = backpack[i][0]
        v = backpack[i][1]
        if j < w :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)

print(dp[n][k])