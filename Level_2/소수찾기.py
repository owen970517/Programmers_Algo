import itertools

def solution(numbers):
    answer = 0
    li=[]
    per = []
    number=''
    prime_numbers=[]
    for i in range(len(numbers)):
        if numbers[i] not in ['0','1'] :
            li.append(numbers[i])
    for i in range(1,len(numbers)+1):
        nCr = itertools.permutations(numbers, i)
        per.append(list(set(nCr)))
    for i in range(len(per)):
        print(per[i])


    return answer,numbers,li,per

numbers = '17'
print(solution(numbers))