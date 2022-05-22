import itertools
# 조합을 사용하지 않고 구한 코드 
""" def solution(numbers):
    answer = []
    numbers.sort()
    li=[]
    for i in range(len(numbers)):
        sum=0
        for j in range(i+1,len(numbers)):
            sum = numbers[i] +numbers[j]
            li.append(sum)
    answer=list(set(li))
    return answer """

def solution(numbers):
    answer = []
    numbers.sort()
    nCr = list(itertools.combinations(numbers,2))
    for i in nCr:
        answer.append(i[0]+i[1])
    answer=sorted(list(set(answer)))
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))

