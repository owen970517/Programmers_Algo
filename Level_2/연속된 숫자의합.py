def solution(n) :
    answer=0
    for i in range(1,n+1) :
        sum = 0
        sum += i
        if sum == n :
            answer += 1
        for j in range(i+1,n+1) :
            sum += j
            if(sum == n) :
                answer += 1
                break
            elif sum > n :
                break
    return answer
print(solution(15))