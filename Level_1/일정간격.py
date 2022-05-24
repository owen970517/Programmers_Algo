def solution(x, n):
    answer = []
    if x <0 :
        ran = range(x,n*x-1,x)
    elif x ==0:
        ran = range(x,n,)
    else:
        ran = range(x,n*x+1,x)
    for i in ran:
            answer.append(i)

    return answer

x = 0
n = 3
print(solution(x,n))