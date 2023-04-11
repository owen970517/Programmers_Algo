def solution(sequence) :
    answer = []
    li=  []
    li2 = []
    for i in range(len(sequence)) :
        if i % 2 == 0 :
            li.append(sequence[i] * 1)
            li2.append(sequence[i] * -1)
        else :
            li.append(sequence[i] * -1)
            li2.append(sequence[i] * 1)
    dp1 = [0] * len(sequence)
    dp2 = [0] * len(sequence) 
    for i in range(len(sequence)) :
        if i == 0 :
            dp1[i] = li[0]
            dp2[i] = li2[0]
        else :
            dp1[i] = max(li[i], dp1[i-1]+li[i])
            dp2[i] = max(li2[i], dp2[i-1]+li2[i])
    answer = max(max(dp1),max(dp2))
    return answer

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))