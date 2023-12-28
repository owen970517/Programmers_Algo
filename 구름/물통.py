# from collections import deque

# def F(x, a, b, c):
#     if x == a:
#         return c
#     else:
#         return b

# def E(x):
#     return 0

# def M(x, y, a, c, d):
#     if x == a:
#         if x <= d - y:
#             y += x
#             x = 0
#         else:
#             x -= (d - y)
#             y = d
#     else:
#         if x <= c - y:
#             y += x
#             x = 0
#         else:
#             x -= (c - y)
#             y = c
#     return x, y

# a, b, c, d = map(int, input().split())

# na, nb = 0, 0
# cnt = 0
# q = deque()
# q.append((na, nb, cnt))
# visited = [[False] * (b + 1) for _ in range(a + 1)]
# visited[na][nb] = True

# while q:
#     a, b, cnt = q.popleft()
#     if (a, b) == (c, d):
#         print(cnt)
#         break
#     if not visited[F(a, a, b, c)][b]:
#         visited[F(a, a, b, c)][b] = True
#         q.append((F(a, a, b, c), b, cnt + 1))
#     if not visited[a][F(b, a, b, c)]:
#         visited[a][F(b, a, b, c)] = True
#         q.append((a, F(b, a, b, c), cnt + 1))
#     if not visited[E(a)][b]:
#         visited[E(a)][b] = True
#         q.append((E(a), b, cnt + 1))
#     if not visited[a][E(b)]:
#         visited[a][E(b)] = True
#         q.append((a, E(b), cnt + 1))
#     na, nb = M(a, b, a, c, d)
#     if 0 <= na <= a and 0 <= nb <= b and not visited[na][nb]:
#         visited[na][nb] = True
#         q.append((na, nb, cnt + 1))

#     na, nb = M(b, a, b, c, d)
#     if 0 <= na <= a and 0 <= nb <= b and not visited[na][nb]:
#         visited[na][nb] = True
#         q.append((na, nb, cnt + 1))

# print(cnt)

from collections import deque

def bfs(a, b, c,d):
    queue = deque([(0, 0)])
    visited[0][0] = True
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (c,d):
            return cnt
        li = [(0, y), (x, 0), (a, y), (x, b)]
        
        for nx, ny in [(0, y), (x, 0), (a, y), (x, b)]:
            if 0<= nx <= a and 0 <= ny<=b and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
        cnt += 1
    return -1

a, b, c, d = map(int, input().split())
visited = [[False]*(b + 1) for _ in range(a + 1)]
print(bfs(a, b, c,d) // 2)

# (x - min(x, b - y), y + min(x, b - y)), (x + min(a - x, y), y - min(a - x, y))

if x <= b-y :
    y += x
    x = 0
else :
    x -= (b-y)
    y = b
