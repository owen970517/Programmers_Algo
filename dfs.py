graph = [[1, 8], [0, 2, 4], [1], [4], [1, 3, 6], [6], [5, 4], [8], [0, 7, 9], [10, 11, 8], [9], [9]]
# 방문노드
def dfs(graph, v, visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 0번 노드가 없으니 1번 노드부터 탐색
visited = [False] * (len(graph)+1)
dfs(graph, 0, visited)

# for i in range(6) :
#     visited = [False] * len(graph)
#     dfs(graph, i+1, visited)
#     node = []
#     for j in range(len(visited)) :
#         if visited[j] == True :
#             node.append(j)
#     if node not in answer :
#         answer.append(node)
