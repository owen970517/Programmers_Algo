n,m,x,y,k = map(int,input().split())
maps = []
ans = []
dice = [0,0,0,0,0,0]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def roll(d) :
    if d == 1 : # 동
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[0],dice[4],dice[2],dice[5],dice[3],dice[1]
    elif d==2 : #서 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[0],dice[5],dice[2],dice[4],dice[1],dice[3]
    elif d == 3 : #북
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1],dice[2],dice[3],dice[0],dice[4],dice[5]
    else :
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[0],dice[1],dice[2],dice[4],dice[5]

for i in range(n) :
    li = list(map(int,input().split()))
    maps.append(li)
cmd = list(map(int,input().split()))

for i in cmd :
    x += dx[i-1]
    y +=dy[i-1]
    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[i-1]
        y -= dy[i-1]
        continue
    roll(i)
    if maps[x][y] == 0 :
        maps[x][y] = dice[3]
    else :
        dice[3] = maps[x][y]
        maps[x][y] = 0
    
    print(dice[1])

