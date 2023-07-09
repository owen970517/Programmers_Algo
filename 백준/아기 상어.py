from collections import deque


def bfs(x,y,cnt,size) :
    global eat_cnt
    q = deque()
    q.append((x,y,cnt,size))

    while q :
        x,y,cnt,size = q.popleft()
        if x == ex and y == ey :
            return visited[x][y]
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                if 0< li[nx][ny] <size :
                    eat_cnt += 1
                    if eat_cnt == size :
                        eat_cnt = 0
                        q.append((nx,ny,cnt+1,size+1))
                        visited[nx][ny] = visited[x][y] +1
                    else :
                        q.append((nx,ny,cnt+1,size))
                        visited[nx][ny] = visited[x][y] +1
                elif li[nx][ny] == size :
                    q.append((nx,ny,cnt+1,size))
                    visited[x][y] + 1
    
    return cnt

n = int(input())
li = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
eat_cnt = 0
for i in range(n):
    s = list(map(int,input().split()))
    li.append(s)
food = []
visited = [[0] * n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if li[i][j] == 9 :
            sx,sy = i,j
            break
        elif 0< li[i][j] < 9 :
            food.append((i,j))
print(food[0][0],food[0][1])
if len(food) == 1 :
    ex,ey = food[0][0],food[0][1]
    bfs(sx,sy,0,2)
else :
    print(bfs(sx,sy,0,2))