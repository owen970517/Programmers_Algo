from collections import deque

def bfs() :
    global cnt
    while q :
        z,x,y = q.popleft()
        for i in range(6) :
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nz<h and 0<=nx<m and 0<=ny<n and farm[nz][nx][ny] == 0 :
                farm[nz][nx][ny] = farm[z][x][y] + 1
                q.append((nz,nx,ny))

n,m,h = map(int,input().split())
farm = []
dz = [0, 0, 0, 0, -1, 1]
dx = [0, 0, 1, -1,0,0]
dy = [1, -1, 0, 0,0,0]
q = deque()
cnt = 0

for i in range(h) :
    tmp = []
    for j in range(m) :
        s = list(map(int,input().split()))
        tmp.append(s)
    farm.append(tmp)

for i in range(h) :
    for j in range(m) :
        for k in range(n) :
            if farm[i][j][k] == 1 :
                q.append((i,j,k))
bfs()

for i in farm :
    for j in i :
        if 0 in j :
            print(-1)
            exit(0)
        else :
            cnt = max(cnt,max(j))

print(cnt-1)


