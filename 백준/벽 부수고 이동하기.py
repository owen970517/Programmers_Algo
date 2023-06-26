from collections import deque

def bfs(x,y,wall) :
    q = deque()
    q.append((x,y,wall))

    while q :
        x,y,wall = q.popleft()

        if x == n-1 and y == m-1 :
            return visited[x][y][wall]
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0<= ny < m and visited[nx][ny][wall] == 0 :
                if li[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][wall+1] = visited[x][y][wall] +1
                    q.append((nx,ny,wall+1))
                elif li[nx][ny] == 0 :
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx,ny,wall))
    return -1

n,m = map(int,input().split())
li =[]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
for i in range(n) : 
    s = list(map(int,input()))
    li.append(s)
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
print(bfs(0,0,0))

