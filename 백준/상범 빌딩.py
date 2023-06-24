from collections import deque

def bfs() :
    q = deque()
    q.append((sz,sy,sx))
    while q :
        z,y,x = q.popleft()
        if li[z][y][x] == 'E' :
            return "Escaped in {0} minute(s).".format(visited[z][y][x])
        for i in range(6) :
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and visited[nz][ny][nx] == 0:
                if li[nz][ny][nx] == "." or li[nz][ny][nx] == "E":
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nz,ny,nx))
    return 'Trapped!'

while 1 :
    l,r,c = map(int,input().split())
    if l==0 and r==0 and c == 0 :
        break
    li = [[] * c for _ in range(l)]
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    for i in range(l) :
        for _ in range(r) :
            s = list(map(str,input().strip()))
            li[i].append(s)
        input()

    for i in range(l) :
        for j in range(r) :
            for k in range(c) :
                if li[i][j][k] == 'S' :
                    sx,sy,sz = k,j,i
    print(bfs())

# from collections import deque

# def bfs(x,y,z) :
#     q = deque()
#     q.append((x,y,z))
#     while q :
#         x,y,z = q.popleft()
#         for i in range(6) :
#             nx = x+dx[i]
#             ny = y+dy[i]
#             nz = z+dz[i]
#             if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
#                 if li[x][y][z] == 'E' :
#                     return "Escaped in {0} minute(s).".format(visited[x][y][z])
#                 if li[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:
#                     visited[nx][ny][nz] = visited[x][y][z] + 1
#                     q.append([nx, ny, nz])
#     return 'Trapped!'

# while 1 :
#     l,r,c = map(int,input().split())
#     if l==0 and r==0 and c == 0 :
#         break
#     li = [[[]*c for _ in range(r)] for _ in range(l)]
#     visited = [[[0]*c for _ in range(r)] for _ in range(l)]
#     dx = [1, -1, 0, 0, 0, 0]
#     dy = [0, 0, -1, 1, 0, 0]
#     dz = [0, 0, 0, 0, 1, -1]
#     for i in range(l):
#         li[i] = [list(map(str, input().strip())) for _ in range(r)]
#         input()
#     for i in range(l):
#         for j in range(r):
#             for k in range(c):
#                 if li[i][j][k] == 'S':
#                     print(bfs(i, j, k))