n, m = map(int, input().split())
grid = [['.'] * m for _ in range(n)]
x, y = 0, 0
isRight = True

while 0 <= x < n and 0 <= y < m:
    grid[x][y] = '#'
    
    if isRight and (y == m - 1 or (x < n-1 and grid[x+1][y] == '#')):
        isRight = False
        if x + 1 < n:
            grid[x + 1][y] = '#'
        if x + 2 < n:
            grid[x + 2][y] = '#'
        x += 2
    elif not isRight and (y == 0 or (x < n-1 and grid[x+1][y] == '#')):
        isRight = True
        if x + 1 < n:
            grid[x + 1][y] = '#'
        if x + 2 < n:
            grid[x + 2][y] = '#'
        x += 2
    else:
        y = y + 1 if isRight else y - 1

for row in grid:
    print(''.join(row))