def solution(arr) :
    answer = 0
    for i in arr :
        for j in range(1,len(i)) :
            answer += i[j]-i[j-1]
    return answer

print(solution([[1,2],[3,5],[6,7]]))