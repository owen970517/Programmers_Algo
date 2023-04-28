import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = True
    li[x][y] = 0
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[nx][ny] =='.':
            continue
        if visited[nx][ny] == False :
            dfs(nx,ny)

t = int(input())
for i in range(t) :
    li = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    h,w = map(int,input().split())
    cnt = 0
    visited = [[False] * w for _ in range(h)]
    for j in range(h) :
        s = list(input())
        li.append(s)
    for a in range(h) :
        for b in range(w) :
            if li[a][b] =='#' :
                dfs(a,b) 
                cnt += 1
    print(cnt)