def solution(game_board,table) :
    answer = -1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False] * len(game_board) for _ in range(len(game_board))]
    table_puzzule = []
    def dfs(x,y,puzzle):
        visited[x][y] = True
        puzzle.append(table[x][y])
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=len(table) or ny<=-1 or ny>=len(table[0]) or table[nx][ny] == 0:
                continue
            else :
                if visited[nx][ny] == False and table[nx][ny] == 1 :
                    dfs(nx,ny,puzzle)
                    visited[nx][ny] = True
    for i in range(len(table)) :
        for j in range(len(table)) :
            puzzle = []
            if table[i][j] == 1 :
                dfs(i,j,puzzle)
                print(puzzle)
    print(table_puzzule)

    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
               [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))