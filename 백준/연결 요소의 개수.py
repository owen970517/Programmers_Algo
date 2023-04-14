import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
cnt = 0
visited = [False] * (n+1)
for i in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,n+1) :
    if not visited[i] :
        dfs(i)
        cnt +=1
print(cnt)
