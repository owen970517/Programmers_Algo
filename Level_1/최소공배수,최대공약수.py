import math


def solution(n, m):
    answer = []
    a,b=n,m
    while m > 0:
        n, m = m, n % m
    gcd=n
    answer.append(gcd)    
    lcm=a*b//gcd
    answer.append(lcm)
    return answer

n=2
m=5
print(solution(n,m))