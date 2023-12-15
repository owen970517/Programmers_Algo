def game(y,x) :
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    cnt = 0
    isEnd = False
    while not isEnd :
        now = li[y][x]
        count = int(now[:len(now)-1])
        cmd = now[-1]
        dy,dx = d[cmd][0],d[cmd][1]
        for _ in range(count) :
            y = (y+dy)%n
            x = (x+dx)%n
            cnt += 1
            if visited[y][x] :
                isEnd = True
                break
            visited[y][x] = True
    return cnt

n = int(input())
g = list(map(int,input().split()))
p = list(map(int,input().split()))
sg,eg = g[0]-1,g[1]-1
sp,ep = p[0]-1,p[1]-1
d = {
    'D' :[1,0],
    'U' :[-1,0],
    'L' :[0,-1],
    'R' : [0,1]
}
li = []
for i in range(n) :
    cmd = list(input().split())
    li.append(cmd)  

g_score = game(sg,eg)
p_score = game(sp,ep)

if g_score > p_score :
    print('goorm',g_score)
else :
    print('player',p_score)
