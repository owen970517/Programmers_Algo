def solution(land) :
    answer = 0
    for i in range(1,len(land)) :
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    answer = max(land[len(land)-1])
    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# def solution(land) :
#     answer = 0
#     sum = max(n[0])
#     now_index = n[0].index(max(n[0]))
#     for i in range(1,len(n)) :
#         now_max = max(n[i][:now_index])
#         now_index = n[i].index(now_max)
#         sum += now_max
#     answer = sum
#     return answer