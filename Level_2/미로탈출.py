# from collections import deque

# def bfs(x,y,maze) :
#     queue = deque()
#     queue.append((x,y))
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     cnt = 0
#     while queue :
#         x,y = queue.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[0]) or maze[nx][ny] == 'X':
#                 continue
#             if maze[nx][ny] == 'O' or maze[nx][ny] == 'L' or maze[nx][ny] =='E':
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

def bfs(x,y,visited,maze) :
    queue = deque()
    queue.append((x,y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[0]) or maze[nx][ny] == 'X':
                continue
            else :
                maze[nx][ny] = 'X'
                cnt += 1
                visited[nx][ny] = cnt
                queue.append((nx,ny))
    return cnt
def solution(maps) :
    answer = 0 
    maze = []
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    for i in maps :
        maze.append(list(i))
    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            if maze[i][j] == 'S' :
                x,y = i,j
                break
    maze[x][y] = 'X'
    bfs(x,y,visited,maze)
    print(visited)
    print(maze)
    answer = max(visited)

    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))