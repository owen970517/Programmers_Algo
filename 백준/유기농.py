from collections import deque


def bfs(x,y) :
    li[x][y] = 0
    q = deque()
    q.append((x,y))
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and li[nx][ny] == 1 :
                li[nx][ny] = 0 
                q.append((nx,ny))
        
t = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(t) :
    cnt = 0
    m,n,k = map(int,input().split())
    li = [[0] * n for _ in range(m)]
    for _ in range(k) :
        x,y = map(int,input().split())
        li[x][y] = 1
    for i in range(m) :
        for j in range(n) :
            if li[i][j] == 1 :
                li[i][j] = 0
                bfs(i,j)
                cnt += 1
    print(cnt)