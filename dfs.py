graph = [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
# 방문노드
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# 0번 노드가 없으니 1번 노드부터 탐색
# dfs(graph, 6, visited)
answer = []
for i in range(6) :
    visited = [False] * len(graph)
    dfs(graph, i+1, visited)
    node = []
    for j in range(len(visited)) :
        if visited[j] == True :
            node.append(j)
    if node not in answer :
        answer.append(node)
print(len(answer))