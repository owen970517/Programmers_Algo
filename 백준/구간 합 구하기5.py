import sys
input = sys.stdin.readline

n,m = map(int,input().split())
li = list(map(int,input().split()))
dp = [0] * (n+1)
total = 0
for i in range(1,n+1) :
    total += li[i-1]
    dp[i] = total

for _ in range(m) :
    i,j = map(int,input().split())
    now = dp[j]-dp[i-1]
    print(now)