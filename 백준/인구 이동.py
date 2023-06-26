from collections import deque

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    total = li[x][y]
    union  = [(x,y)]
    while q :
        x,y= q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l<=abs(li[nx][ny]-li[x][y]) <=r :
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    union.append((nx,ny))
                    total += li[nx][ny]
    for i in union :
        li[i[0]][i[1]] = total//len(union)
    
    return len(union)
n,l,r = map(int,input().split())
li=[]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    s = list(map(int,input().split()))
    li.append(s)
ans = 0
while 1 :
    visited = [[False] * n for _ in range(n)]
    move = False
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                if bfs(i,j) > 1:
                    move = True
    if not move :
        break
    ans += 1
print(ans)