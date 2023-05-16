from collections import deque

def solution(n,results) :
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i in results :
        graph[i[1]].append(i[0])
    print(graph)
    visited = [1] * (n+1)
    print(visited)

    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))