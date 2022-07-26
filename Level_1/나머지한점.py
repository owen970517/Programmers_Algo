def solution(v):
    answer = []
    li = []
    li2 = []
    for i in v :
        li.append(i[0])
        li2.append(i[1])
    for i in li :
        if li.count(i) <2 :
            answer.append(i)
    for i in li2 :
        if li2.count(i) < 2 :
            answer.append(i)
    return answer,li,li2

v = [[1, 1], [2, 2], [1, 2]]
print(solution(v))