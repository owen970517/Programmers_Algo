def solution(n,left,right) :
    answer = []
    for i in range(left , right +1) :
        answer.append(max(i%n , i//n)+1)
    return answer

print(solution(3,2,5))

""" 내가 푼 풀이 시간 초과가 발생 
def solution(n,left,right) :
    answer = 0
    arr = [[0] * n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if i ==0 and j == 0:
                arr[i][j] = j+1
            elif j==0 or i ==j or i > j :
                arr[i][j] = i+1
            elif i < j :
                arr[i][j] = j+1
    for i in arr :
        for j in i :
            result.append(j)
    answer = result[left:right+1]
    return answer """