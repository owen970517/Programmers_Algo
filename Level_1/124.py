def solution(n):
    arr=['1','2','4']
    answer=''
    while n>0:
        n-=1
        answer = arr[n%3]+answer
        n//=3
    return answer
n=10
print(solution(n))