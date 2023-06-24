# 수정한 풀이
from collections import deque

def bfs() :
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and li[nx][ny] == 0 :
                li[nx][ny] = li[x][y] + 1
                q.append((nx,ny))


n,m = map(int,input().split())
li = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q= deque()
for i in range(m):
    s = list(map(int,input().split()))
    li.append(s)
    
for i in range(m) :
    for j in range(n) :
        if li[i][j] == 1 :
            q.append((i,j))
bfs()
day = 0
for i in li :
    if 0 not in i :
        day = max(day,max(i))
    else :
        day = -1
        break
if day > 0 :
    print(day-1)
else :
    print(day)

# 테케는 다 통과하지만 제출하면 틀리다고 나옴 
# from collections import deque

# def bfs(x,y) :
#     q=deque()
#     q.append((x,y))
#     while q :
#         x,y = q.popleft()
#         for i in range(4) :
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0<=nx<m and 0<=ny<n and li[nx][ny] == 0 :
#                 li[nx][ny] = li[x][y] + 1
#                 q.append((nx,ny))

# n,m = map(int,input().split())
# li = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# for i in range(m):
#     s = list(map(int,input().split()))
#     li.append(s)
    
# for i in range(m) :
#     for j in range(n) :
#         if li[i][j] == 1 :
#             bfs(i,j)
# day = 0
# for i in li :
#     if 0 not in i :
#         day = max(day,max(i))
#     else :
#         day = -1
#         break
# if day > 0 :
#     print(day-1)
# else :
#     print(day)