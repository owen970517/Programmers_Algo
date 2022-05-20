
def solution(a, b):
    answer = 0
    sum=0
    if a >b:
        a,b=b,a
    for i in range(a,b+1):
        sum+=i
    answer=sum
    return answer

a,b=3,5
print(solution(a,b))