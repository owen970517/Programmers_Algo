def solution(wallpaper) :
    answer = []
    row =[]
    col = []
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[i])) :
            if wallpaper[i][j] == '#' :
                if i not in row or j not in col :
                    row.append(i)
                    col.append(j)
    row = list(set(row))
    col = list(set(col))
    li = [min(row) , min(col) ,max(row) + 1 , max(col) + 1]
    answer = li
    return answer

print(solution(["..", "#."]))