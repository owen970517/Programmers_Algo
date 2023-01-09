def solution(babbling) :
    answer = 0
    can =['aya','ye','woo','ma']
    cant = ['ayaaya','yeye','woowoo','mama']
    li = []
    for i in babbling :
        for k in cant :
            i= i.replace(k , 'X')
        for j in can :
            if j =='aya' :
                i = i.replace(j,'A')
            elif j =='ye' :
                i= i.replace(j,'B')
            elif j =='woo' :
                i = i.replace(j,'C')
            elif j == 'ma' :
                i = i.replace(j,'D')
        if i.isupper() :
            li.append(i)
    for i in li :
        if i.find('X') != 0 :
            answer += 1
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))