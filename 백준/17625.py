import sys
sys.setrecursionlimit(1000000)

def dfs(x,y,now,prev):
    global max_answer,min_answer
    if x == n-1 and y == n-1 :
        min_answer = min(int(now),min_answer)
        max_answer = max(int(now),max_answer)
    
    for i in range(2) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=len(li) or ny>=len(li[0]):
            continue
        else :
            if visited[nx][ny] == False :
                visited[nx][ny] =True
                if li[nx][ny].isdigit() :
                    total = str(eval(now + prev + li[nx][ny]))
                    dfs(nx,ny,total,'')
                else :
                    dfs(nx,ny,now,li[nx][ny])
                visited[nx][ny] = False
n = int(input())
li = []
dx = [0,1]
dy = [1,0]
max_answer = -float("inf")
min_answer = float("inf")
visited = [[False] * n for _ in range(n)]
for i in range(n) :
    s = list(input().split())
    li.append(s)

visited[0][0] = True
dfs(0,0,li[0][0],'')
print(max_answer,min_answer)