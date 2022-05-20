def solution(n):
    answer = 0
    li=[]
    while n>0:
        n,na = divmod(n,3)
        li.insert(0,na)
    li.reverse()
    for i in reversed(range(len(li))):
        answer += 3**i * li[len(li)-1-i]
    return answer

n=int(input())
print(solution(n))