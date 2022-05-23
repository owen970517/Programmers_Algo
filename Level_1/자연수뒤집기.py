def solution(n):
    answer = []
    n= str(n)
    li = list(n)
    for i in reversed(li):
        answer.append(int(i))
    return answer

n = 12345
print(solution(n))