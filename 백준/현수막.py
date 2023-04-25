def dfs(x,y) :
    visited[x][y] = True
    banner[x][y] = 0
    for i in range(8) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(banner) or ny<=-1 or ny>=len(banner[0]):
            continue
        else :
            if visited[nx][ny] == False :
                if banner[nx][ny] == 1 :
                    dfs(nx,ny)  


n,m = map(int,input().split())
banner = []
dx = [0, 0, 1, -1,1,-1,1,-1]
dy = [1, -1, 0, 0,1,1,-1,-1]
cnt = 0
visited = [[False] * m for _ in range(n)]
for i in range(n) :
    s = list(map(int,input().split())) 
    banner.append(s)

for i in range(n) :
    for j in range(m) :
        if banner[i][j] == 1 :
            dfs(i,j)
            cnt += 1

print(cnt)