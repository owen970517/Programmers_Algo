import sys
sys.setrecursionlimit(10**9)   

input = sys.stdin.readline
def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1
for i in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(graph, r, visited)
print(*visited[1:] , sep='\n')
