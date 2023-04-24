import sys
sys.setrecursionlimit(1000000)

def dfs(x,y):
    if li[x][y] == '-' :
        li[x][y] = '1'
        for i in range(2) :
            ny = y+dy[i]
            if ny<=-1 or ny>=len(li[0]):
                continue
            else :
                if li[x][ny] == '-' :
                    dfs(x,ny)
    elif li[x][y] == '|' :
        li[x][y] == '1'
        for i in range(2) :
            nx = x + dx[i]
            if nx<=-1 or nx>=len(li) :
                continue
            else :
                if li[nx][y] == '|' :
                    dfs(nx,y)

n,m = map(int,input().split())
li = []
dx = [1,-1]
dy = [1,-1]
for i in range(n) :
    s = list(input())  
    li.append(s)
cnt = 0
for i in range(n) :
    for j in range(m) :
        if li[i][j] != '1':
            dfs(i,j)
            cnt += 1
print(li)
print(cnt)