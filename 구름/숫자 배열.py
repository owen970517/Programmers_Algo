n = int(input())
li = [[0] * n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if i > 0  and j == 0 :
            li[i][j] = li[i-1][j] + n
        else :
            li[i][j] = li[i][j-1] + 1
print(li)