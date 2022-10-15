import itertools

def solution(X, Y):
    answer = ''
    list = []
    for i in (set(X) and set(Y)) :
        for _ in range(min(X.count(i), Y.count(i))) :
            list.append(i)
    list.sort(reverse=True)
    print(list)
    if len(list) == 0 :
        return '-1'
    elif list[0] == '0' :
        return '0'
    answer = ''.join(list)
    return answer

print(solution("5525", "1255"))
