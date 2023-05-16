# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(x,y) :
#     q = deque()
#     q.append((x,y))
#     while q :
#         x,y = q.popleft()
#         if x == end[0] and y == end[1] :
#             return li[x][y]
#         for i in range(8) :
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) :
#                 continue
#             else :
#                 li[nx][ny] = li[x][y] + 1
#                 q.append((nx,ny))
# t = int(input())
# dx=[1,-1,2,-2,2,1,-1,-2]
# dy=[2,2,1,1,-1,-2,-2,-1]
# for i in range(t) :
#     l = int(input())
#     li = [[0] * l for _ in range(l)]
#     start = list(map(int,input().split()))
#     end = list(map(int,input().split()))
#     print(bfs(start[0],start[1]))

from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx, sy, ex, ey):
    q = deque()
    q.append([sx, sy])
    while q:
        a, b = q.popleft()
        if a == ex and b == ey:
            return li[ex][ey]
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < l and 0 <= y < l and li[x][y] == 0:
                q.append([x, y])
                li[x][y] = li[a][b] + 1
t = int(input())
for i in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    li = [[0] * l for _ in range(l)]
    print(bfs(sx, sy, ex, ey))