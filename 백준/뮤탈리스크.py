from itertools import permutations


n = int(input())
scv = list(map(int,input().split()))
dp = [[[61] * 61 for _ in range(61)] for _ in range(61)]
damage = [9,3,1]
comb = list(permutations(damage,3))
hits = 1e9

while len(scv) < 3 :
    scv.append(0)

def dfs(x,y,z) :
    global hits 
    if x ==y== z == 0:
        hits = min(hits, dp[x][y][z])
        return 
    for i in comb :
        nx = x - i[0]
        ny = y - i[1]
        nz = z - i[2]
        if nx <0 :
            nx = 0
        if ny < 0 :
            ny =0
        if nz <0:
            nz = 0
        if dp[nx][ny][nz] > dp[x][y][z] + 1:
            dp[nx][ny][nz] = dp[x][y][z] + 1
            dfs(nx, ny, nz)

dp[scv[0]][scv[1]][scv[2]] = 0  
dfs(scv[0],scv[1],scv[2])
print(hits)
