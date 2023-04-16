import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,width) :
    visited[x][y] = True
    li[x][y] = 2
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]):
            continue
        else :
            if visited[nx][ny] == False :
                if li[nx][ny] == 0 :
                    width += 1
                    width = dfs(nx,ny,width) 
    return width
n,m,k = map(int,input().split())
li = []
w_li = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * m for _ in range(n)] 
for i in range(n) :
    li.append([0] * m)
for _ in range(k) :
    x,y,x1,y1 = map(int,input().split())
    for i in range(y,y1) :
        for j in range(x,x1) :
            li[i][j] = 1
li = li[::-1]
width = 1
for i in range(n) :
    for j in range(m) :
        if li[i][j] == 0 :
            w_li.append(dfs(i,j,width))
            
print(len(w_li))
w_li.sort()
print(*w_li)
