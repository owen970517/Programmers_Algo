# from collections import deque

# def bfs(x,y,maps) :
#     queue = deque()
#     queue.append((x,y))
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     cnt = 0
#     if maze[x][y] == 'L' :
#         return
#     while queue :
#         x,y = queue.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[0]) or maze[nx][ny] == 'X':
#                 continue
#             else :
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx,ny))
#     return cnt
# def solution(maps) :
#     answer = 0 
#     maze = []
#     for i in maps :
#         maze.append(list(i))
#     for i in range(len(maps)) :
#         for j in range(len(maps[i])) :
#             if maze[i][j] == 'S' :
#                 x,y = i,j
#                 break
#     maze[x][y] = 0
#     answer = bfs(x,y,maze)
#     print(maze)
#     print(maze[-1][-1])
#     if answer == 0 :
#         return -1

#     return answer

from collections import deque

def bfs(start,visited,maps,target) :
    queue = deque()
    queue.append(start)
    visited[start[1]][start[0]]= True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    while queue :
        x,y = queue.popleft()
        if maps[y][x] == target :
            return cnt
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or maps[ny][nx] == 'X':
                continue
            else :
                if visited[ny][nx] == False :
                    visited[ny][nx] = True
                    cnt += 1
                    queue.append((nx,ny))
    return -1
def solution(maps) :
    answer = 0 
    maps = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i in maps :
        maps.append(list(i))
    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            if maps[i][j] == 'S' :
                start = (j,i)
            if maps[i][j]=='L' :
                lever = (j,i)
    lever_len = bfs(start,visited,maps,'L')
    end_len = bfs(lever,visited,maps,'E')
    if lever_len == -1 or end_len == -1 :
        answer = -1
    else :
        answer= lever_len + end_len

    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))