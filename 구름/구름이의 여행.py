from collections import deque


n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [-1] * (n+1)
def bfs(now) :
    q = deque()
    q.append(now)
    visited[now] = 0
    while q :
        now = q.popleft()

        for i in graph[now] :
            if visited[i] != -1 :
                continue
            q.append(i)
            visited[i] = visited[now] + 1
bfs(1)
if 1 <= visited[n] <= k :
    print("YES")
else :
    print("NO")
