def solution(n, arr1, arr2):
    answer = []
    li=[]
    li2=[]
    result=[]
    for i in arr1:
        li.append(bin(i)[2:].zfill(n))
    for i in arr2:
        li2.append(bin(i)[2:].zfill(n))
    for i in range(n):
        ans=""
        for j in range(n):
            if li[i][j] == '1' or li2[i][j] =='1':
                ans +='1'
            else:
                ans+='0'
        result.append(ans)
    for i in result:
        i=i.replace('1','#')
        i=i.replace('0',' ')
        answer.append(i)
    return answer
  
n = 6
arr1 =[46, 33, 33 ,22, 31, 50]
arr2= [27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))