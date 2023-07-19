def solution(m, n, board):
    answer = 0
    board = list(map(list,board))
    while 1 :
        visited = [[0] * n  for _ in range(m)]
        for i in range(m-1) :
            for j in range(n-1):
                if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1] and board[i][j] != '0' :
                    visited[i][j],visited[i][j+1],visited[i+1][j],visited[i+1][j+1] = 1,1,1,1
        if visited == [[0] * n  for _ in range(m)] :
            break
        for i in range(m) :
            for j in range(n) :
                if visited[i][j] == 1 :
                    answer += 1
                    board[i][j] = '0' 
        while True:
            moved = False
            
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != '0' and board[i+1][j] == '0':
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        moved = True 
            
            if not moved: 
                break

    return answer

m=6
n=6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m,n,board))