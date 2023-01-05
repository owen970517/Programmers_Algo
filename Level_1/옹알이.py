from itertools import permutations

def solution(babbling) :
    answer = 0
    can =['aya','ye','woo','ma']
    cant = ['ayaaya','yeye','woowoo','mama']
    li = []
    for i in babbling :
        for j in cant :
            i = i.replace(j , 'A')
        for k in can :
            i = i.replace(k,'B')
        for char in i:
            if char != "B":
                isValid = False
                break
        if isValid == True:
            answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa"]))