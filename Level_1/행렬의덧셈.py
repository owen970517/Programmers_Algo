def solution(arr1, arr2):
    answer =[]
    for i in range(len(arr1)):
        li=[]
        for j in range(len(arr2[0])):
            a=arr1[i][j] + arr2[i][j]
            li.append(a)
        answer.append(li) 
    return answer

arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]
print(solution(arr1,arr2))