def solution(n) :
    answer = 0
    if n == 0:
        answer = 0
    elif n == 1 :
        answer = 1
    elif n>=2 :
        answer = solution(n-1) + solution(n-2)
    return answer

print(solution(5))