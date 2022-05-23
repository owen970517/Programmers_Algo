def solution(n):
    answer = 0
    result = ""
    n =str(n)
    li = list(n)
    li.sort(reverse=True)
    for i in li:
        result +=i
    answer = int(result)
    return answer

n = 118372
print(solution(n))