import sys
sys.setrecursionlimit(1000000)

def dfs(x,y):
    global s_cnt,princess
    if len(princess) < 7 :
        princess.append(li[x][y])
    else :
        princess = []
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) :
            continue
        else :
            if len(princess) < 7 :
                dfs(nx,ny)



li=[]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
princess = []
ans = 0
for i in range(5) :     
    s = list(input())   
    li.append(s)
visited = [[False] * 5 for _ in range(5)]
for i in range(5) :
    for j in range(5) :
        s_cnt = 0
        dfs(i,j)
        print(princess)
        for s in princess :
            if s == 'S' :
                s_cnt += 1
                print(s_cnt)
        if s_cnt >= 4 :
            ans += 1
print(ans)