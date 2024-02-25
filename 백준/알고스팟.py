from collections import deque

n,m = map(int,input().split())
li = []
for i in range(m) :
    s = list(input())
    li.append(s)

q = deque()
q.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[-1] * (n) for _ in range(m)]
visited[0][0] = 0

while q :
    x,y = q.popleft()
    if (x,y) == (m-1,n-1) :
        print(visited[x][y])
        break
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0  or nx>=m or ny < 0 or ny>=n :
            continue
        if visited[nx][ny] == -1 :
            if li[nx][ny] == '0' :
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx,ny)) # 벽이 없는 곳을 우선시하는 이 부분을 생각하지 못했음 
            else :
                visited[nx][ny] = visited[x][y] +1
                q.append((nx,ny))
