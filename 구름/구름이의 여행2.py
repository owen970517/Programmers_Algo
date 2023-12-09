from collections import deque

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)

visited = [-1] * (n+1)
def bfs(v) :
    q = deque()
    q.append(v)
    visited[v] = 1
    while q :
        now = q.popleft()

        for next in graph[now] :
            if visited[next] != -1 and next != k :
                continue
            if next == k :
                return visited[now]
            q.append(next)
            visited[next] = visited[now] + 1
    return -1
print(bfs(k))

# 시간 초과 
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# N, M, K = map(int, input().split())

# graph = [[INF] * (N+1) for _ in range(N+1)]
# for a in range(1, N+1):
#     for b in range(1, N+1):
#         if a == b:
#             graph[a][b] = 0

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] = 1

# for k in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# if min(graph[K][i] + graph[i][K] for i in range(1, N+1) if i != K) >= INF:
#     print(-1)

# else:
#     print(min(graph[K][i] + graph[i][K] for i in range(1, N+1) if i != K))
