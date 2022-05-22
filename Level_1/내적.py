def solution(a, b):
    answer = 1234567890
    dot =0
    for i in range(len(a)):
        dot += a[i] * b[i]
    answer=dot
    return answer

a = [1,2,3,4]
b=	[-3,-1,0,2]
print(solution(a,b))