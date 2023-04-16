graph = [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
# 방문노드
def dfs(graph, v, visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 0번 노드가 없으니 1번 노드부터 탐색
visited = [False] * len(graph)
dfs(graph, 4, visited)
answer = []
# for i in range(6) :
#     visited = [False] * len(graph)
#     dfs(graph, i+1, visited)
#     node = []
#     for j in range(len(visited)) :
#         if visited[j] == True :
#             node.append(j)
#     if node not in answer :
#         answer.append(node)
print(len(answer))