def solution(n,computers) :
    answer = 0
    visited = [0] * n
    def dfs(i) :
        visited[i] = 1
        for j in range(n) :
            print(computers[i][j])
            if computers[i][j] == 1 and visited[j] == 0 :
                dfs(j)

    for i in range(n) :
        if visited[i] == 0  :
            dfs(i)
            print(visited)
            answer += 1
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))