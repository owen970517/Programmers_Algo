# 내가 푼 풀이
# def solution(board) :
#     answer = -1
#     first = 0
#     back = 0
#     for i in board :
#         for j in range(len(list(i))) :
#             if i[j] == 'O' :
#                 first += 1
#             elif i[j] == 'X' :
#                 back += 1
#     if first ==0 and back == 0 :
#         answer = 1
#     elif first >= back and first <3 and back<3 and first-back <= 1: 
#         answer = 1
#     elif first > back and first+back == 9 :
#         answer = 1
#     else :
#         answer= 0
#     return answer

def won(board, t):
    # 가로줄 판단.
    for row in board:
        if row == [t, t, t]:
            return True
        
    # 세로줄 판단.
    for col in range(3):
        if [board[row][col] for row in range(3)] == [t, t, t]:
            return True
        
    # 대각선 판단.
    if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [t, t, t]:
        return True
    
    return False

def solution(board) :
    answer = -1
    first = 0
    back = 0
    new = []
    for i in board :
        new.append(list(i))
        for j in range(len(i)) :
            if i[j] == 'O' :
                first += 1
            elif i[j] == 'X' :
                back += 1
    isOwin = won(new,'O')
    isXwin = won(new,'X')
    if first ==0 and back == 0 :
        answer = 1
    if first < back :
        answer = 0
    if not isOwin and not isXwin and first-back <= 1 :
        answer = 1
    if isOwin and not isXwin and first-back == 1 :
        answer = 1
    if isXwin and not isOwin and first==back :
        answer = 1
    else :
        answer= 0
    return answer
print(solution(["OXO", "OX.", ".X."]))