def solution(arr):
    answer = 0
    sum=0
    for i in arr:
        sum +=i
    answer=sum/len(arr)
    return answer

arr = [1,2,3,4]
print(solution(arr))