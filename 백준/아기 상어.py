# from collections import deque

# def bfs(x,y) :
#     q = deque()
#     q.append((x,y,0))
#     visited = [[False] * n for _ in range(n)]
#     dis = []
#     visited[x][y] = True
#     min_dis = int(1e9)
#     while q :
#         x,y,dist = q.popleft()
#         for i in range(4) :
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
#                 if li[nx][ny] <= size :
#                     visited[nx][ny] = True
#                     if 0< li[nx][ny] < size :
#                         min_dis = dist
#                         dis.append((dist+1,nx,ny))
#                     if dist+1 <= min_dis :
#                         q.append((nx,ny,dist+1))
#     if dis :
#         dis.sort()
#         return dis[0]
#     else :
#         return False
    

# n = int(input())
# li = []
# dx = [-1, 1, 0, 0] 
# dy = [0, 0, -1, 1]
# eat_cnt = 0
# size = 2
# for i in range(n):
#     s = list(map(int,input().split()))
#     li.append(s)

# for i in range(n) :
#     for j in range(n) :
#         if li[i][j] == 9 :
#             sx,sy = i,j

# li[sx][sy] = 0
# ans = 0
# while 1 :
#     res = bfs(sx,sy)
#     if not res :
#         break
#     sx,sy = res[1],res[2]
#     ans += res[0]
#     eat_cnt += 1

#     if size == eat_cnt :
#         size += 1
#         eat_cnt = 0
#     li[sx][sy] = 0

# print(ans)
from collections import deque


def bfs(x,y) :
    global size
    distance = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    eat_fish = []
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] :
                if li[nx][ny] <= size :
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    if li[nx][ny] < size and li[nx][ny] != 0 :
                        eat_fish.append((nx,ny,distance[nx][ny]))

    return sorted(eat_fish,key=lambda x:(-x[2],-x[0],-x[1]))

n = int(input())
li = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
eat_cnt = 0
ans = 0
size = 2
for i in range(n):
    s = list(map(int,input().split()))
    li.append(s)

for i in range(n) :
    for j in range(n) :
        if li[i][j] == 9 :
            sx,sy = i,j


while 1 :
    res = bfs(sx,sy)
    if len(res) == 0 :
        break
    nx,ny,d = res.pop()
    ans += d
    li[sx][sy],li[nx][ny] = 0,0

    sx,sy=nx,ny
    eat_cnt += 1
    if eat_cnt == size :
        size += 1
        eat_cnt = 0

print(ans)