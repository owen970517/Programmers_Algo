from collections import deque

def solution(maps) :
    answer = 0
    n = len(maps)
    m=len(maps[0])
    dx = [-1,1,0,0]
    dy=[0,0,-1,1]
    def bfs(x,y) :
        queue = deque()
        queue.append((x,y))
        while queue :
            x,y = queue.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny <0 or ny >=m :
                    continue
                if maps[nx][ny] == 0 :
                    continue
                if maps[nx][ny] == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
                    print(queue)
        return maps[n-1][m-1]
    result = bfs(0,0)
    if result == 1 :
        answer = -1
    else :
        answer = result
    return answer 

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

