from collections import deque


n = int(input())
li = []
dx = [-1,1,0,0]
dy=[0,0,-1,1]
cnt = 0
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)

def bfs(x,y) :
    q =deque()
    q.append((x,y))
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx< 0 or ny >= n or ny < 0 :
                continue
            if li[nx][ny] == 1 :
                q.append((nx,ny))
                li[nx][ny] = 2
                
print(li)

for i in range(n) :
    for j in range(n) :
        if li[i][j] == 1 :
            li[i][j] = 2
            bfs(i,j)
            cnt += 1
print(cnt)