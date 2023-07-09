def quad_tree(x,y,n) :
    global ans
    now = li[x][y]

    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if li[i][j] != now :
                ans.append('(')
                quad_tree(x,y,n//2)
                quad_tree(x,y+n//2,n//2)
                quad_tree(x+n//2,y,n//2)
                quad_tree(x+n//2,y+n//2,n//2)
                ans.append(')')
                return
    ans.append(str(now))

n = int(input())
li = []
ans = []
for _ in range(n):
    li.append(list(map(int, list(input()))))

quad_tree(0,0,n)
print(''.join(ans))