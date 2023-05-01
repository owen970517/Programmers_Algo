# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v,end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

n,m,x = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# print(graph)
# visited = [False] * (len(graph) + 1)
li = []
for i in range(m) :
    a,b = map(int,input().split())
    li.append(a)
    li.append(b)
print(list(set(li)))
