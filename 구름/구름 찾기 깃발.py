from collections import deque


n,k= map(int,input().split())

li = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,-1,1,1,1,-1,-1]
dy=[-1,1,0,0,1,-1,1,-1]

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    cnt = 0
    for i in range(8) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n :
            continue
        if li[nx][ny] == 1 :
            cnt += 1
    return cnt
ans = 0
for i in range(n) :
    for j in range(n) :
        if li[i][j] == 0 :
            now = bfs(i,j)
            if now == k :
                ans += 1
print(ans)
