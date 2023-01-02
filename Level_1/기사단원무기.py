def solution(number,limit,power) :
    answer = 0
    li = [] 
    sum= 0
    for n in range(1,number+1) :
        divisors = []
        for i in range(1, int(n**(1/2)) + 1): 
            if (n % i == 0):            
                divisors.append(i)
                if (i != (n // i)): 
                    divisors.append(n//i)
        li.append(len(divisors))
    for i in li :
        if i > limit :
            answer += power
        else :
            answer += i  
    return answer,li

print(solution(10,3,2))
