import math

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if math.pow(i,2) == n:
            answer = int(math.pow(i+1,2))
            break
        else :
            answer = -1
    return answer

n = 121
print(solution(n))