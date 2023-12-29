from collections import deque


def bfs(v) :
    q = deque()
    q.append(v)
    visited = [v]
    while q :
        v = q.popleft()
        for i in graph[v] :
            if i not in visited :
                ans[i] = ans[v]+1
                visited.append(i)
                q.append(i)
    return sum(ans)
n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

res = []

for i in range(1,n+1) :
    ans = [0] * (n+1)
    res.append(bfs(i))
    
print(res.index(min(res))+1)

