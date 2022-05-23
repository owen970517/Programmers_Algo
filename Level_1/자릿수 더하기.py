def solution(n):
    answer = 0
    n=str(n)
    li = list(n)
    for i in n:
        answer +=int(i)
    return answer

n =123
print(solution(n))