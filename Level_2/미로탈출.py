from collections import deque

def bfs(x,y,maze) :
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
            if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[i]) or maze[nx][ny] == 'X':
                continue
            else :
                print(maze[nx][ny])
                maze[nx][ny] = 'X'
                cnt += 1
                queue.append((nx,ny))
    return cnt
def solution(maps) :
    answer = 0 
    maze = []
    for i in maps :
        maze.append(list(i))
    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            if maze[i][j] == 'S' :
                x,y = i,j
                break
    maze[x][y] = 'X'
    answer = bfs(x,y,maze)
    if answer == 0 :
        return -1

    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))