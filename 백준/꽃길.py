# 유사한 문제 : 연구소, 치킨배달,감시 피하기
from itertools import combinations

def dfs(li) :
    global ans 
    total =0
    visited =[[False] * n for _ in range(n)]
    for x,y in li :
        visited[x][y] = True
        total += board[x][y]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<=-1 or nx>=len(board) or ny<=-1 or ny>=len(board[0]) or visited[nx][ny] == True:
                return
            else :
                if visited[nx][ny] == False :
                    visited[nx][ny] = True
                    total += board[nx][ny]
    ans = min(ans,total)

n = int(input())
board=[]
for i in range(n) :
    s = list(map(int,input().split()))
    board.append(s)
ans = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
nCr = [(i,j) for i in range(1, n-1) for j in range(1, n-1)]
for li in combinations(nCr, 3):
    dfs(li)
print(ans)
