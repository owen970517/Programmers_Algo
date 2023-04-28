from collections import deque

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= len(li) or ny < 0 or ny >= len(li[0]) or li[nx][ny] == 0 :
                continue
            if li[nx][ny] == 1 :
                li[nx][ny] = li[x][y] + 1
                queue.append((nx,ny))
    return li[-1][-1]

n,m = map(int,input().split())
li = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
for i in range(n) :
    s = list(map(int,input()))   
    li.append(s)
print(bfs(0,0))
