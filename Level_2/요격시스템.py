def solution(target) :
    answer = 0
    target = sorted(target,key=lambda x : x[1])
    prev = target[0][1]
    answer += 1
    for i in range(1,len(target)) :
        if target[i][0] >= prev :
            answer += 1
            prev = target[i][1]
    return answer
print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))
