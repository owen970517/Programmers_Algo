from collections import deque

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    now = li[x][y]
    re_li = [(x,y)]
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 or li[nx][ny] != now or visited[nx][ny]:
                continue
            if not visited[nx][ny] and li[nx][ny] == now :
                q.append((nx,ny))
                visited[nx][ny] = True
                re_li.append((nx,ny))
    return re_li

N,K,Q = map(int,input().split())
li = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(N) :
    s = list(input())
    li.append(s)


for i in range(Q) :
    visited = [[False] * N for _ in range(N)]
    y,x,d = input().split()
    y,x = int(y),int(x)
    li[y-1][x-1] = d
    res = bfs(y-1,x-1)
    if len(res) >= K :
        for r,c in res :
            li[r][c] = '.'
for i in li :
    print(''.join(i))