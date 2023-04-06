from collections import deque

def bfs(x,y,board) :
    visited = [[float("inf")] * len(board[0]) for i in range(len(board))]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        fx,fy = x,y
        for i in range(4):
            x,y = fx,fy # 반복을 할 때마다 x랑 y가 변한채로 진행이 되니 첫 시작을 다시 넣어줘야 한다.
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 > nx or nx == len(board) or 0 > ny or ny == len(board[0]) or board[nx][ny] == 'D':
                    if board[x][y] == 'G':
                        return visited[fx][fy] + 1
                    if visited[fx][fy] + 1 < visited[x][y] : 
                        q.append((x,y))
                        visited[x][y] = visited[fx][fy] + 1
                    break
                x,y = nx,ny
    return -1

def solution(board) :
    answer = 0
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if board[i][j] == 'R' :
                x,y = i,j
    answer = bfs(x,y,board)
    return answer
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))