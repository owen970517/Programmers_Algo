from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[-1] * 102 for i in range(102)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in rectangle :
        x1,y1,x2,y2 = map(lambda x : x*2,i)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)]
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
    return answer

print(solution([[1,1,5,7]],1,1,4,7))