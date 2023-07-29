def solution(board,skill) :
    answer = len(board) * len(board[0])
    tmp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board) + 1)] 
 
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]

    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            if board[i][j] <= 0:
                answer -= 1
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

# def solution(board,skill) :
#     answer = 0
#     total = len(board) * len(board[0])
#     for k in skill :
#         if k[0] == 1 :
#             for i in range(k[1],k[3]+1) :
#                 for j in range(k[2],k[4]+1) :
#                     board[i][j] -= k[5]
#                     if board[i][j] + k[5] > 0 and board[i][j] <=0 :
#                         total -= 1
#         else :
#             for i in range(k[1],k[3]+1) :
#                 for j in range(k[2],k[4]+1) :
#                     board[i][j] += k[5]
#                     if board[i][j] - k[5] <= 0 and board[i][j] > 0 :
#                         total += 1
#     answer= total
#     return answer