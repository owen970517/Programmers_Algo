from collections import deque


def bfs(x,y) :
    q = deque()
    q.append((x,y))
    while q :
        x,y= q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0<=ny <m and li[nx][ny] == 1 :
                li[nx][ny] = li[x][y] + 1
                q.append((nx,ny))
        
n,m = map(int,input().split())
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
li = []
for i in range(n) :
    s = list(map(int,input()))
    li.append(s)
bfs(0,0)
print(li[-1][-1])


