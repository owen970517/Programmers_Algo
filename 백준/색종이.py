n = int(input())
board = [[0]* 100 for _ in range(100)]
sum =0
for _ in range(n) :
    x,y = list(map(int,input().split()))
    for i in range(x,x+10) :
        for j in range(y,y+10) :
            board[i][j] = 1

for i in board :
    sum += i.count(1)
print(sum)