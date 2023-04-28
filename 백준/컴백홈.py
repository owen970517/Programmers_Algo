import sys
sys.setrecursionlimit(1000000)

def dfs(x,y,cnt) :
    global answer
    visited[x][y] = True
    if x == 0 and y == c-1 :
        if cnt == k :
            answer += 1
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[nx][ny] == 'T':
            continue
        else :
            if visited[nx][ny] == False :
                visited[nx][ny] = True
                dfs(nx,ny,cnt+1)
                visited[nx][ny] = False   

r,c,k= map(int,input().split())
li = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * c for _ in range(r)]
answer = 0
for i in range(r) :
    s = list(map(str,input()))
    li.append(s)
dfs(r-1,0,1)
print(answer)