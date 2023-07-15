def hanoi(n,start,end,mid,answer) :
    if n == 1 :
        answer.append([start,end])
    else :
        hanoi(n-1,start,mid,end,answer)
        answer.append([start,end])
        hanoi(n-1,mid,end,start,answer)
def solution(n) :
    answer = []
    hanoi(n,1,3,2,answer)
    return answer

print(solution(4))