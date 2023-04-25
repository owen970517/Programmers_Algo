def solution(cards) :
    answer= 0
    visited = [False] * (len(cards)+1)
    box_group = []
    for i in cards :
        if not visited[i] :
            li = []
            while i not in li :
                li.append(i)
                i = cards[i-1]
                visited[i] = True
            box_group.append(li)
    box_group.sort(reverse=True)
    if len(box_group) == 1 :
        return 0
    else :
        answer = len(box_group[0])* len(box_group[1])
    return answer

print(solution([8,6,3,7,2,5,1,4])) 