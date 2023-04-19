import sys
sys.setrecursionlimit(10 ** 8)

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    ans[v] = cnt
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
cnt = 1
for i in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph :
    i = i.sort(reverse=True)
dfs(graph,r,visited)
for i in ans[1:] :
    print(i)


