from collections import deque


def water_fall(x, y):
    global water
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 1 :
            water.append((nx,ny))

def sand_island(x,y) :
    q = deque()
    q.append((x,y))
    sand_visited[x][y] = True
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 1 and not sand_visited[nx][ny]:
                sand_visited[nx][ny] =True          
                q.append((nx,ny))

n,m = map(int,input().split())
li = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
time = 0
while 1 :
    if li == [[0] * m for _ in range(n)] :
        print(-1)
        break
    water = []
    time += 1
    for i in range(n) :
        for j in range(m) :
            if li[i][j] == 0 :
                water_fall(i,j)

    for x,y in water :
        li[x][y] = 0

    cnt = 0
    sand_visited = [[False] * m for _ in range(n)]
    for i in range(n) :
        for j in range(m) : 
            if li[i][j] == 1 and not sand_visited[i][j] :
                sand_island(i,j)
                cnt += 1  
    if cnt >= 2 :
        print(time)
        break