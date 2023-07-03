def dfs(x,y,d) :
    global cnt

    if li[x][y] == 0 and not visited[x][y] :
        visited[x][y] = True
        cnt += 1
    for _ in range(4) :
        nd = (d+3) % 4
        nx = x+dx[nd] 
        ny = y+dy[nd]
        if li[nx][ny] == 0 and not visited[nx][ny] :
            dfs(nx,ny,nd) 
            return
        d = nd
    nd = (d+2) % 4
    nx = x+dx[nd]
    ny = y+dy[nd]

    if li[nx][ny] == 1 :
        return cnt
    dfs(nx,ny,d)
n,m = map(int,input().split())
x,y,d = map(int,input().split())
li = []
cnt = 0
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
visited = [[False] * m for _ in range(n)]

dfs(x,y,d)
print(cnt)

