def solution(a,b,n) :
    answer = 0
    while 1 :
        answer += n//a * b
        if n < a :
            break
        n = n- (n//a *a ) + (n//a * b)
    return answer

print(solution(3,1,20)) 