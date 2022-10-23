def solution(array):
    answer = 0
    while True :
        a = array.pop(0)
        b = array.pop(0)
        for i in range(max(a, b), (a * b) + 1):
            if i % a == 0 and i % b == 0:
                result = i
                break
        array.insert(0,result)
        if len(array) == 1 :
            answer = array[0]
            break
                
    return answer
print(solution([2,6,8,14]))