def solution(board, moves):
    answer = 0
    li=[]
    line1,line2,line3,line4,line5=[],[],[],[],[]
    basket=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if j ==0 and board[i][j] != 0:
                line1.append(board[i][j])
            elif j==1 and board[i][j] != 0:
                line2.append(board[i][j])
            elif j ==2 and board[i][j] != 0:
                line3.append(board[i][j])
            elif j==3 and board[i][j] != 0:
                line4.append(board[i][j])
            elif j==4 and board[i][j] != 0:
                line5.append(board[i][j])
    for i in moves:
        if i ==1:
            if len(line1) ==0:
                basket.append(0)
            else:
                basket.append(line1.pop(0))
        elif i==2:
            basket.append(line2.pop(0))
        elif i==3:
            basket.append(line3.pop(0))
        elif i ==4:
            basket.append(line4.pop(0))
        elif i==5:
            basket.append(line5.pop(0)) 
    if len(basket) > 1:
        basket.pop()
        basket.pop()
        answer+=2
    return answer,line1,line2,line3,line4,line5,basket,li
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
print(solution(board,moves))