import sys
sys.setrecursionlimit(1000000)

def dfs(x,y):
    visited[x][y] = True
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<=-1 or nx>=len(RGB) or ny<=-1 or ny>=len(RGB[0]):
            continue
        else :
            if visited[nx][ny] == False :
                if RGB[nx][ny] == RGB[x][y] :
                    dfs(nx,ny)
n = int(input())
RGB = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
redgreen_cnt =0
for i in range(n) :
    RGB.append(list(input()))
print(RGB)
visited = [[False] * n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            dfs(i,j)
            cnt +=1

visited = [[False] * n for _ in range(n)]
for i in RGB :
    for j in range(len(i)) :
        if i[j] == 'G' :
            i[j] = 'R'
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            dfs(i,j)
            redgreen_cnt +=1           
print(cnt,redgreen_cnt)
