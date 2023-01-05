def solution(storey) :
    answer = 0
    while storey :
        i = storey%10
        if i > 5 :
            storey += 10 - i
            answer += 10 - i
        elif i ==5 and storey//10 >= i :
            storey += 10-i
            answer += 10-i 
        else :
            storey -= i
            answer += i
        storey = storey // 10 
    return answer

print(solution(95))

