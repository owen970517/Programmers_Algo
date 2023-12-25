from collections import deque


def bfs(x,y) :
    q = deque()
    q.append((x,y))
    v = 1
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or li[nx][ny] == '.':
                continue
            v+= 1
            li[x][y] = '.'
            li[nx][ny] = '.'
            print(li)
            q.append((nx,ny))
    return v


n,m =map(int,input().split())
li = [list(input()) for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = 0
for i in range(m) :
    for j in range(n) :
        if li[i][j] == '#' :
            cnt += 1
            ans = max(ans,bfs(i,j))
print(cnt)
print(ans)