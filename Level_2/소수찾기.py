import itertools
import math

def solution(numbers):
    answer = 0
    li=[]
    per = []
    prime_numbers=[]
    for i in range(len(numbers)):
        li.append(numbers[i])
    for i in range(1,len(numbers)+1):
        nCr = itertools.permutations(numbers, i)
        per += list(nCr)
    for i in per :
        prime = ("").join(i)
        prime_numbers.append(int(prime))
    prime_numbers = list(set(prime_numbers))
    for i in prime_numbers :
        if i < 2 :
            continue
        is_prime = True
        for n in range(2, int(math.sqrt(i)) + 1):
            if i % n == 0:
                is_prime = False
                break
        if is_prime:
            answer +=1
    return answer,prime_numbers

numbers = '17'
print(solution(numbers))