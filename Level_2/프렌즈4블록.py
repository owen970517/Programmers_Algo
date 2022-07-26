def solution(m, n, board):
    answer = 0
    for i in range(len(board)-1) :
        print(i)
        for j in range(len(board)):
            print(j)
            print(board[i][j],board[i][j+1] , board[i+1][j] , board[i+1][j+1])
    return answer,board

m=4
n=5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))