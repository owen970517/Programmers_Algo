def solution(card) :
    answer =[]
    li = []
    sort_card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for i in card :
        idx = sort_card.index(i)
        li.append(idx)
    li = sorted(li)
    for i in li :
        answer.append(sort_card[i])
        
    return answer

print(solution(['A','Q','K','J']))