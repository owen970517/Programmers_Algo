def dfs(x,y):
    queue = [(x,y)]
    field[x][y] = 0
    while queue :
        x,y =queue.pop(0)
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if field[nx][ny] == 1 :
                queue.append((nx,ny))
                field[nx][ny] = 0

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(t) :
    field = []
    cnt = 0
    n,m,k = map(int,input().split())
    for i in range(n) :
        field.append([0] * m)
    for i in range(k) :
        x,y = map(int,input().split())
        field[x][y] = 1
    for i in range(n) :
        for j in range(m) :
            if field[i][j] == 1 :
                dfs(i,j)
                cnt +=1
    print(cnt)