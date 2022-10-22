def solution(arr) :
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            total = 0
            total +=sum(arr[j:i+j+1])
            if (len(arr[j:i+j+1]) < i+1) :
                total += sum(arr[:i+1-len(arr[j:i+j+1])])
            answer.append(total)
    answer = list(set(answer))
    return len(answer)

print(solution([7,9,1,1,4]))
