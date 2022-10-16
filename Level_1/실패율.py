def solution(N,stages) :
    answer= []
    result = {}
    k= len(stages)
    for i in range(1,N+1) :
        if k ==0 :
            result[i] = 0 
        else :
            result[i] = stages.count(i)/k
            k -= stages.count(i)
    answer = sorted(result, key=lambda x: result[x], reverse=True)
    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))