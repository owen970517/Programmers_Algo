def solution(numbers, target):
    answer = 0
    result = [0]
    for i in numbers:
        tmp = []
        for j in result:
            tmp.append(j + i)
            tmp.append(j - i)
        result = tmp
    for n in result:
        if n == target:
            answer += 1
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))




