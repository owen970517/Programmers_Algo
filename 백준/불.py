# from collections import deque

# def bfs():
#     cnt = 0
#     while q:
#         while fire and fire[0][2] < cnt:
#             x, y, time = fire.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < h and 0 <= ny < w:
#                     if li[nx][ny] == "." or li[nx][ny] == "@":
#                         li[nx][ny] = "*"
#                         fire.append((nx, ny, time + 1))

#         while q and q[0][2] < cnt:
#             x, y, time = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < h and 0 <= ny < w:
#                     if li[nx][ny] == "." and not visited[nx][ny]:
#                         visited[nx][ny] = True
#                         q.append((nx, ny, time + 1))
#                 else:
#                     return cnt

#     return "IMPOSSIBLE"


# t = int(input())
# dx = [-1, 1, 0, 0] 
# dy = [0, 0, -1, 1]

# for i in range(t) :
#     li = []
#     q=deque()
#     fire=deque()
#     w,h = map(int,input().split())
#     visited = [[False] * w for _ in range(h)]
#     for i in range(h) :
#         s = list(input())
#         li.append(s)
#         for j in range(w) :
#             if s[j] == '@' :
#                 visited[i][j]=True
#                 q.append((i,j,0))
#             elif s[j] == '*' :
#                 fire.append((i,j,0))
#     print(bfs())
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if li[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])
                elif nx < 0 or ny < 0 or nx >= h or ny >= w:
                    return visited[x][y]
            qlen -= 1
        fire()

    return "IMPOSSIBLE"

def fire():
    qlen = len(fq)
    while qlen:
        x, y = fq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if li[nx][ny] == '.':
                    li[nx][ny] = '*'
                    fq.append([nx, ny])
        qlen -= 1

t = int(input())
for i in range(t) :
    w, h = map(int, input().split())
    li = [list(map(str, input().strip())) for _ in range(h)]
    fq, q = deque(), deque()
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if li[i][j] == '@':
                sx ,sy =i, j
                
            if li[i][j] == '*':
                fq.append([i, j])
    fire()
    print(bfs(sx, sy))
    