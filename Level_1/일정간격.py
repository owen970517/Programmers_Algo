def solution(x, n):
    answer = []
    ran =[]
    if x <0 :
        ran = range(x,n*x-1,x)
    elif x ==0:
        for i in range(x,n) :
            ran.append(0)
    else:
        ran = range(x,n*x+1,x)
    for i in ran:
            answer.append(i)

    return answer

x = 2
n = 5
print(solution(x,n))