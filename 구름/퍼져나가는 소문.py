n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = []
def dfs(graph, v, visited):
    visited[v] = True
    ans.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (len(graph)+1)

dfs(graph, 1, visited)
print(len(ans))

