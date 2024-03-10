from collections import deque

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x +dx[i]
            ny = y+dy[i]
            if 0<= nx < len(li) and 0<=ny<len(li[0]) and li[nx][ny] == 1 :
                q.append((nx,ny))
                li[nx][ny] = li[x][y] + 1
    return li[-1][-1]
n,m = map(int,input().split())
li = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
for i in range(n) :
    now = list(map(int,input()))
    li.append(now)

print(bfs(0,0))

