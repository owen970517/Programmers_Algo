def dfs(x,y,word) :
    word += str(li[x][y])
    if len(word) == 6 :
        if word not in ans :
            ans.append(word)
            word = ''
        return 
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx < 0 or nx>=5 or ny < 0 or ny>=5:
            continue
        else :
            dfs(nx,ny,word)
li = []
word =''
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []
for i in range(5) :
    s = list(map(int,input().split()))
    li.append(s)
for i in range(5) :
    for j in range(5) :
        dfs(i,j,word)
print(len(ans))