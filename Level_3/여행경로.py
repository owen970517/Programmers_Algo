# def solution(tickets) :
#     answer =[]
#     tickets.sort(key=lambda x : x[1])
#     dic = dict([])
#     visited = dict()
#     for i in tickets :
#         dic[i[0]],dic[i[1]] = [],[]
#         visited[i[0]],visited[i[1]] = [],[]
#     for i in tickets :
#         dic[i[0]].append(i[1])
#         visited[i[0]].append(False)
#     print(dic)
#     def dfs(graph, v):
#         answer.append(v)
#         print(answer)
#         for idx,i in enumerate(graph[v]):
#             print(i)
#             if not visited[v][idx] :
#                 visited[v][idx] = True
#                 dfs(graph, i)
#     dfs(dic,'ICN')
#     return answer

def solution(tickets):
    answer = []
    visited = [False]*len(tickets)
    def dfs(airport, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                print(path+[ticket[1]])
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False
        
        
    dfs("ICN", ["ICN"])
    
    answer.sort()

    return answer[0]
print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))