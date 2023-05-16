import sys
import copy
sys.setrecursionlimit(1000000)

def dfs(x,y):
    li_copy[x][y] = 0
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) :
            continue
        else :
            if li_copy[nx][ny] > k :
                dfs(nx,ny)
n = int(input())
li = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
maxNum =0
for i in range(n) :
    s = list(map(int,input().split()))
    maxNum = max(maxNum,max(s))
    li.append(s)
ans = 0
for k in range(maxNum) :
    cnt = 0
    li_copy = copy.deepcopy(li)
    for i in range(n) :
        for j in range(n) :
            if li_copy[i][j] > k :
                dfs(i,j)
                cnt += 1
    ans = max(ans,cnt)
print(ans)
