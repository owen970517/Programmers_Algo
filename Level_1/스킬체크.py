def solution(arr, location):
    answer=""
    find =arr[location]
    cnt=0
    for i in range(len(arr)-1):
        J=arr[0]
        if arr[i+1] >= J:
            n= arr.pop(0)
            arr.append(n)
            cnt+=1 
    for i in arr:
        if i == find:
            answer=(arr.index(i))+1
    return answer,arr,cnt

    

arr =[1, 1, 9, 1, 1, 1]
#[1, 1, 9, 1, 1, 1] ,0
print(solution(arr, 0))