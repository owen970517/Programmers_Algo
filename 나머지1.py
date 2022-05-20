
def solution(n):
    answer = 0
    for i in range(1,1000000):
        if n%int(i)==1:
            answer = int(i)
            break
    return answer

n = int(input())
print(solution(n))