def solution(n,costs) :
    answer = 0
    costs.sort(key=lambda x:x[2])
    print(costs)
    graph = set([costs[0][0]])

    while len(graph) != n :
        for i in costs :
            if i[0] in graph and i[1] in graph :
                continue
            if i[0] in graph or i[1] in graph :
                graph.update([i[0],i[1]])
                answer += i[2]
                break
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))