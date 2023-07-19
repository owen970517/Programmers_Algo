from collections import deque

def solution(n,edge) :
    answer = 0
    graph = [[] for i in range(len(edge)+1)]
    for i in edge :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    print(graph)
    visited = [0] * (n+1)
    visited[1] = 1
    def bfs(graph, v, visited):
        q = deque([v])
        while q :
            v = q.popleft()
            for i in graph[v]:
                if not visited[i]:
                    q.append(i)
                    print(visited)
                    visited[i] = visited[v] + 1
                    print(visited)
    bfs(graph, 1, visited)
    answer = visited.count(max(visited))
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))