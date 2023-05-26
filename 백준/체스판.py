n,m = map(int,input().split())
board = []
ans = []
for i in range(n) :
    s = list(input())
    board.append(s)

for i in range(n-7) :
    for j in range(m-7) :
        start_w = 0
        start_b = 0
        for a in range(i,i+8) :
            for b in range(j,j+8) :
                if (a+b) % 2 ==0 : # 홀수인 경우
                    if board[a][b] != 'W' :
                        start_w += 1
                    if board[a][b] != 'B' :
                        start_b += 1
                else : # 짝수인 경우 
                    if board[a][b] != 'B' :
                        start_w += 1
                    if board[a][b] != 'W' :
                        start_b += 1
        ans.append(min(start_w,start_b))
print(min(ans))
