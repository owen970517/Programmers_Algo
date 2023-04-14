def dfs(x,y) :
    visited[x][y] = True
    li[x][y] = 0
    for i in range(8) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]):
            continue
        else :
            if visited[nx][ny] == False :
                if li[nx][ny] == 1 :
                    dfs(nx,ny)     
while 1 :
    n,m = map(int,input().split())
    if n == 0 and m == 0 :
        break
    li = []
    dx = [0, 0, 1, -1,1,-1,1,-1]
    dy = [1, -1, 0, 0,1,1,-1,-1]
    visited = [[False] * n for _ in range(m)]
    cnt = 0
    print(visited)
    for i in range(m) :
        s = list(map(int,input().split()))
        li.append(s)
    for i in range(m) :
        for j in range(n) :
            if li[i][j] == 1 :
                dfs(i,j)
                cnt += 1
    print(cnt)
