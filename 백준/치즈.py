from collections import deque

def bfs() :
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    cheeze = 0
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] :
                visited[nx][ny] = True
                if graph[nx][ny] == 0 :
                    q.append((nx,ny))
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = 0
                    cheeze += 1
    return cheeze


n,m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
total = 0
time = 1
for i in range(n) : 
    s = list(map(int,input().split()))
    graph.append(s)
    total += s.count(1)
while 1 :
    visited = [[False] * m for _ in range(n)]
    now = bfs()
    print(now)
    total -= now
    if total == 0 :
        print(time)
        print(now)
        break
    time += 1
    
