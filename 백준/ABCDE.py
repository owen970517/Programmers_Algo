def dfs(graph, v, visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [False] * len(graph)
print(graph)
for i in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
dfs(graph, 0, visited)