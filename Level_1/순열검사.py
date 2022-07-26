def solution(arr) :
    answer = True
    new_li=[]
    arr.sort()
    for i in range(1,len(arr)+1) :
        if i ==arr[i-1] :
            answer= True
        else :
            answer = False
    return answer

arr = [4, 1, 3]
print(solution(arr))