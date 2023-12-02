from collections import deque

def solution(board,h,w) :
    answer = 0
    cnt = 0
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    def bfs(x,y,cnt) :

        queue = deque()
        queue.append((x,y))
        while queue :
            x,y = queue.popleft()
            for i in range(4) :
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or board[nx][ny] == 0 :
                    continue
                if board[nx][ny] == board[h][w] :
                    cnt += 1
        return cnt
    answer = bfs(h,w,cnt)
    return answer

print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]],0,1
    ))