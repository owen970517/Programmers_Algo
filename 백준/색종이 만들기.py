def quad_tree(x,y,n) :
    global blue,white
    now = li[x][y]

    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if li[i][j] != now :
                quad_tree(x,y,n//2)
                quad_tree(x,y+n//2,n//2)
                quad_tree(x+n//2,y,n//2)
                quad_tree(x+n//2,y+n//2,n//2)
                return
    if now == 0 :
        white += 1
    else :
        blue += 1

n = int(input())
li = []
blue = 0
white = 0

for _ in range(n) :
    s = list(map(int,input().split()))
    li.append(s)

quad_tree(0,0,n)
print(white)
print(blue)
