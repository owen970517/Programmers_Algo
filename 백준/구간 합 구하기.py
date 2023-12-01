import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
li = []
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n) :
    now = list(map(int,input().split()))
    li.append(now)

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + li[i-1][j-1] 

for i in range(m) :
    total = 0 
    x1,y1,x2,y2 = map(int,input().split())
    total = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(total)
