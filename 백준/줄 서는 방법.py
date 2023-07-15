from itertools import combinations, permutations
from math import factorial

def solution(n,k) :
    k -= 1
    answer = []
    li = [i for i in range(1,n+1)]
    for i in range(n, 0, -1):
        div, k = divmod(k,factorial(i-1))
        answer.append(li.pop(div))

    return answer

print(solution(3,5))