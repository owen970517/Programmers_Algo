def solution(arr):
    answer = []
    if len(arr) >1:
        idx=arr.index(min(arr))
        arr.pop(idx)
        answer=arr
    else :
        answer.append(-1)
    return answer

arr = [10]
print(solution(arr))