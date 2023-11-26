from collections import Counter

def solution(str1,str2) :
    answer = 0
    str1 = str1.upper()
    li = []
    str2 = str2.upper()
    li2 = []

    for i in range(len(str1)-1) :
        now = str1[i:i+2]
        if now.isalpha() :
            li.append(now)
    
    for i in range(len(str2)-1) :
        now = str2[i:i+2]
        if now.isalpha() :
            li2.append(now)

    Counter1 = Counter(li)
    Counter2 = Counter(li2)

    a=len(list((Counter1 & Counter2).elements()))
    b=len(list((Counter1 | Counter2).elements()))



    if a == 0 and b == 0 :
        answer = 1 * 65536
    else :
        j = a/b
        answer = int(j*65536)
    return answer

print(solution("FRANCE","french"))