def solution(L, x):
    answer = []
    li=[]
    for i,n in enumerate(L):
        li.append((i,n))
    for i in range(len(li)):
        if li[i][1] == x:
            answer.append(li[i][0])
    if x not in L:
        answer.append(-1)
    return answer

L =  [64, 72, 83, 72, 54] 
x = 49
print(solution(L,x))