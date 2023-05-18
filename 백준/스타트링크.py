import sys
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == G:
            return visited[G]-1
        for i in range(2): 
            n = v+d[i]
            if 0 < n <= F and not visited[n]:
                visited[n] = visited[v] + 1
                q.append(n)
    if visited[G] == 0:
        return "use the stairs"

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
d = [U,-D]
visited = [0] * (F+1)
print(bfs(S))