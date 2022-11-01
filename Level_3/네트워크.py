def solution(n,computers) :
    answer = 0
    visited = [0] * n
    def dfs(i) :
        visited[i] = 1
        for j in range(n) :
            if computers[i][j] and not visited[j] :
                dfs(j)

    for i in range(n) :
        if not visited[i] :
            dfs(i)
            print(visited)
            answer += 1
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))