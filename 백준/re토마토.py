from collections import deque

def bfs() :
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and li[nx][ny] == 0 :
                li[nx][ny] = li[x][y] + 1
                q.append((nx,ny))

m,n = map(int,input().split())
li = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0
for _ in range(n) :
    now = list(map(int,input().split()))
    li.append(now)
q = deque()
for i in range(n) :
    for j in range(m) :
        if li[i][j] == 1 :
            q.append((i,j))
bfs()
flag = False
for i in li :
    if i.count(0) >= 1 :
        flag = True
        break
    else :
        ans = max(ans,max(i))

if flag :
    print(-1)
else :
    if ans == 1 :
        print(0)
    else :
        print(ans-1)