from collections import deque


def solution(board) :
    answer = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    ex,ey = len(board)-1,len(board)-1
    def bfs(x,y,cost,d) :
        q = deque()
        q.append((x,y,cost,d))
        visited= [[int(1e9)] * len(board) for _ in range(len(board))]
        visited[0][0] = 0
        while q :
            x,y,cost,d = q.popleft()
            if x == ex and y == ey :
                continue
            for i in range(4) :
                nx = x +dx[i]
                ny = y+dy[i]
                nd = i 
                if 0<=nx<len(board) and 0<=ny<len(board) and board[nx][ny] != 1 :
                    if nd == d :
                        nc = cost+100
                    else :
                        nc = cost+600
                    if nc < visited[nx][ny] :
                        visited[nx][ny] = nc
                        q.append((nx,ny,nc,nd))

        return visited[-1][-1]
    # 처음에 갈 수 있는 방향은 오른쪽 또는 아래 둘 중에 하나 
    answer = min(bfs(0,0,0,0),bfs(0,0,0,2))

    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))