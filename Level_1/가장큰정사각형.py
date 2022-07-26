def solution(board):
    answer = 1234
    arr = []
    field = []
    for i in range(len(board)) :
        li = []
        for j in range(len(board[0])):
            if board[i][j] == 1 :
                li.append(board[i][j])
        arr.append(li)
    for i in range(len(arr)) :
        if len(arr[i]) >=len(arr[0]) :
            field.append(arr[i])
    answer = len(arr[0]) * len(field)
    return answer

board =[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))