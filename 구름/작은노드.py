n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m) :
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
ans = []
def dfs(graph,v,visited) :
    global cnt,cur
    visited[v] = True
    ans.append(v)
    graph[v].sort()
    for i in graph[v] :
        if not visited[i] :
          dfs(graph,i,visited)
          break     
dfs(graph,k,visited)
print(len(ans), ans[-1])

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# for i in range(m) :
#     u,v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# ans = []
# def dfs(graph, v, visited):
#     visited[v] = True
#     ans.append(v)
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# visited = [False] * (len(graph)+1)

# dfs(graph, 1, visited)
# print(len(ans))

