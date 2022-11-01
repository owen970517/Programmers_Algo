import math 

def solution(n,s) :
    answer = []
    p = s//n
    q = s%n
    result = [p] * n
    if p <= 0 :
        return [-1]
    for i in range(q):
        result[i] += 1
    answer = sorted(result)
    return answer

print(solution(3,11))