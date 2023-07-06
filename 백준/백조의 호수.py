from collections import deque

def bfs() :
    while q :
        x,y = q.popleft()
        if x == x2 and y == y2 :
            return 1
        
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] :
                if li[nx][ny] == '.' :
                    q.append((nx,ny))
                else :
                    q_temp.append((nx,ny))
                visited[nx][ny] = True
    return 0

def melt() :
    while wq :
        x,y = wq.popleft()
        if li[x][y] == 'X' :
            li[x][y] ='.'
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and not w_visited[nx][ny] :
                if li[nx][ny] == 'X' :
                    wq_temp.append((nx,ny))
                else :
                    wq.append((nx,ny))
                w_visited[nx][ny] = True
        



r,c=map(int,input().split())
li = []
swan = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
visited = [[False] * c for _ in range(r)]
w_visited = [[False] * c for _ in range(r)]
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(r) :
    s = list(input())
    li.append(s)
    for j in range(len(s)) :
        if s[j] == 'L' :
            swan.extend([i,j])
            wq.append([i,j])
        elif s[j] == '.' :
            w_visited[i][j] = True
            wq.append([i,j])
    print(swan,wq)
x1, y1, x2, y2 = swan
print(x1,y1,x2,y2)
q.append([x1, y1])
li[x1][y1], li[x2][y2], visited[x1][y1] = '.', '.', True
cnt = 0

while 1 :
    melt()
    if bfs() :
        print(cnt)
        break
    q,wq = q_temp,wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1
