def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if len(arr[i]) < len(arr) :
            arr[i].append(0)
            answer.append(arr[i])
        else :
            answer.append(arr[i])
    if len(answer) < len(arr[0]) :
        for i in range(len(arr[0])-len(answer)) :
            now = [0] * len(arr[0])
            print(now)
            answer.append(now)
    return answer

print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))