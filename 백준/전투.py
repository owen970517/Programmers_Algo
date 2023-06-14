def dfs(x,y) :
    global ally_cnt,enemy_cnt
    if li[x][y] == 'W' and visited[x][y] == False:
        ally_cnt += 1
        visited[x][y] = True
    if li[x][y] == 'B' and visited[x][y]== False:
        enemy_cnt += 1
        visited[x][y] = True
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<=-1 or nx>=len(li) or ny<=-1 or ny>=len(li[0]) or li[x][y] != li[nx][ny]:
            continue
        else :
            if visited[nx][ny] == False :
                dfs(nx,ny)
n,m = map(int,input().split())
li = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
total_ally = 0
total_enemy = 0
ally_cnt = 0
enemy_cnt =0
for i in range(m) :
    s = list(input())
    li.append(s)
visited = [[False] * n for _ in range(m)] 
for i in range(m) :
    for j in range(n) : 
        if visited[i][j] == False :
            dfs(i,j)
            total_ally += ally_cnt**2
            total_enemy += enemy_cnt**2
            ally_cnt,enemy_cnt = 0,0
print(total_ally,total_enemy)