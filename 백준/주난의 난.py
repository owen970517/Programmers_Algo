from collections import deque

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]):
                continue
            else :
                if visited[nx][ny] == -1 :
                    if li[nx][ny] =='1' or li[nx][ny] =='#':
                        visited[nx][ny] = visited[x][y] +1
                        q.append((nx,ny))
                    else:
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx,ny))

n,m = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
li =[]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[-1] * m for _ in range(n)]

for i in range(n) :
    s = list(input())
    li.append(s)

bfs(x1-1,y1-1)
print(visited[x2-1][y2-1])