import sys
sys.setrecursionlimit(111111)

def dfs(k) :
    global ans 
    visited[k] = True
    team.append(k)
    now = li[k]
    if visited[now] :
        if now in team :
            ans += team[team.index(now):]
    else :
        dfs(now)
t = int(input())
for i in range(t) :
    n = int(input())
    li = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    visited[0] = True
    ans = []
    for i in range(1,n+1) :
        if not visited[i]:
            team = []
            dfs(i)
    print(n-len(ans))