from collections import deque

def bfs(x,y,cnt) :
    q = deque()
    temp = []
    for i in li :
        temp.extend(i)
    q.append((x,y,cnt,temp))
    visited = set()
    while q :
        x,y,cnt,checked = q.popleft()
        if checked == default :
            return cnt
        temp = [checked[idx:idx+3] for idx in range(0,7,3)]
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < 3 and 0<=ny<3 :
                temp[x][y],temp[nx][ny] = temp[nx][ny],temp[x][y]
                now =[]
                for i in temp :
                    now.extend(i)
                if tuple(now) not in visited :
                    visited.add(tuple(now))
                    q.append((nx,ny,cnt+1,now))
                temp[x][y],temp[nx][ny] = temp[nx][ny],temp[x][y]
    return -1

li = []
default = [1,2,3,4,5,6,7,8,0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(3) :
    s = list(map(int,input().split()))
    li.append(s)
    for j in range(3) :
        if s[j] == 0 :
            sx,sy = i,j
print(bfs(sx,sy,0))


