def solution(k,ranges) :
    answer = []
    n=0
    li=[]
    li2 = []
    li.append([n,k])
    while k :
        if k == 1 :
            break
        if k % 2 == 0 :
            k= k//2
            n+=1
            li.append([n,k])
        else :
            k = (k*3) +1
            n += 1
            li.append([n,k])
    for i in range(1,len(li)) :
        s = (li[i-1][1] + li[i][1]) * (li[i][0] - li[i-1][0]) / 2
        li2.append(s)
    for i in ranges:
        x=i[0]
        y=len(li2)+i[1]
        if x==y:
            answer.append(0.0)
        elif x>y:
            answer.append(-1.0)
        else:
            answer.append(sum(li2[x:y]))
    return answer,li

print(solution(5,[[0,0],[0,-1],[2,-3],[3,-3]]))