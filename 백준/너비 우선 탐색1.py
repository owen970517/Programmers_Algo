from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
q = deque()
cnt = 1
visited[r] = cnt
for i in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s) :
    global cnt 
    q.append((s))
    while q :
        x = q.popleft()
        graph[x].sort(reverse=True)
        for i in graph[x] :
            if visited[i] == 0 :
                cnt += 1
                visited[i] = cnt
                q.append((i))
bfs(r)

print(*visited[1:] , sep='\n')


