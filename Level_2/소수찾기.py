import itertools

def solution(numbers):
    answer = 0
    li=[]
    per = []
    prime_numbers=[]
    for i in range(len(numbers)):
        li.append(numbers[i])
    for i in range(1,len(numbers)+1):
        nCr = itertools.permutations(numbers, i)
        aa=list(set(nCr))
        per.append(aa)
    for i in per:
        for j in range(len(i)):
            print(j)

    return answer,numbers,li,aa,prime_numbers,per

numbers = '011'
print(solution(numbers))