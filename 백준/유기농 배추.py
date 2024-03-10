from collections import deque

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < m and 0<= ny < n and li[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True

t = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(t) :
    m,n,k = map(int,input().split())
    li = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    cnt = 0

    for _ in range(k) :
        x,y = map(int,input().split())
        li[x][y] = 1

    for i in range(m) :
        for j in range(n) :
            if li[i][j] == 1 and not visited[i][j] :
                bfs(i,j)
                cnt += 1
    print(cnt)