# dfs로 풀었을 때 시간초과 발생 
# def dfs(x,y,cnt) :
#     global ans
#     ans = max(ans,cnt)
#     visited.add(li[x][y])
#     for i in range(4) :
#         nx = x +dx[i]
#         ny = y +dy[i]
#         if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]):
#             continue
#         if 0 <= nx < n and 0 <= ny < m:
#             if li[nx][ny] not in visited:
#                 dfs(nx, ny, cnt + 1)
#                 visited.remove(li[x][y])

import sys
input = sys.stdin.readline
def bfs() :
    global ans
    q = set()
    q.add((0,0,li[0][0]))
    while q :
        x,y,visited = q.pop()
        print(visited)
        ans = max(ans,len(visited))
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]):
                continue
            if li[nx][ny] not in visited :
                q.add((nx,ny,li[nx][ny]+visited))
n,m = map(int,input().split())
li = []
for i in range(n) :
    s = list(input())
    li.append(s)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
bfs()
print(ans)