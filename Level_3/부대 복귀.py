from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    for i in roads :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = 0
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i] == -1:
                    queue.append(i)
                    visited[i] = visited[v] + 1
    bfs(graph,destination,visited)
    for i in sources :
        answer.append(visited[i])

    return answer

print(solution(5,[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],[1,3,5],5))