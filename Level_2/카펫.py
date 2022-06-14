def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(brown, yellow):
    answer = []
    grid = brown + yellow
    divisor=getMyDivisor(grid)
    mid = len(divisor)//2
    for i in range(mid) :
        if (divisor[i]-2) * (divisor[len(divisor)-(i+1)] -2) == yellow :
            answer.append(divisor[i])
            answer.append(divisor[len(divisor)-(i+1)])
            break
    if len(answer) <=0 :
        answer.append(divisor[mid])
        answer.append(divisor[mid])
    answer.sort(reverse=True)
    return answer,divisor
brown =8
yellow =1
print(solution(brown , yellow))


""" 
    def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(brown, yellow):
    answer = []
    grid = brown + yellow
    divisor=getMyDivisor(grid)
    mid = len(divisor)//2
    for i in range(mid) :
        if (divisor[i]-2) * (divisor[len(divisor)-(i+1)] -2) == yellow :
            answer.append(divisor[i])
            answer.append(divisor[len(divisor)-(i+1)])
        else :
            divisor.pop(0)
            divisor.pop()
        if len(divisor) == 1 :
            answer.append(divisor[0])
            answer.append(divisor[0])
    if len(answer) >2 :
        answer = list(set(answer))   
        answer.sort(reverse=True)
    return answer

    """