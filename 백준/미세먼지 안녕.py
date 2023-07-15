import sys
input = sys.stdin.readline

def move(x,y) :
    global cnt
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if 0<=nx<r and 0<=ny<c and li[nx][ny] != -1 :
            visited[nx][ny] += li[x][y] // 5
            cnt += 1

def air_up(ex,ey) :
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    d = 0
    prev = 0 
    sx,sy=up_x,1
    while 1 :
        nx = sx +dx[d]
        ny = sy+dy[d]
        if sx == ex and sy == ey :
            break
        if nx >= r or ny >= c or nx<0 or ny <0:
            d += 1
            continue
        li[sx][sy],prev = prev,li[sx][sy]
        sx,sy = nx,ny

def air_down(ex,ey) :
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    prev = 0
    sx,sy = down_x,1
    while 1 :
        nx = sx+dx[d]
        ny = sy+dy[d]
        if sx == ex and sy == ey :
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue
        li[sx][sy],prev = prev ,li[sx][sy]
        sx,sy = nx,ny


r,c,t = map(int,input().split())
li = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
for i in range(r) :
    s = list(map(int,input().split()))
    li.append(s)

for i in range(r) :
    if li[i][0] == -1 :
        up_x,up_y = i,0
        down_x,down_y = i+1,0
        break

for _ in range(t) :
    visited = [[0] * c for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if li[i][j] > 0:
                cnt = 0
                move(i,j)
                li[i][j] -= (li[i][j]//5) * cnt

    for i in range(r) :
        for j in range(c) :
            li[i][j] += visited[i][j]
    air_up(up_x,up_y)
    air_down(down_x,down_y)

total = 0
for i in li :
    total += sum(i)
print(total+2)

