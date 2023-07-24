from copy import deepcopy


def solution(k,room_number) :
    answer = []
    rooms = [i for i in range(1,k+1)]
    a = deepcopy(rooms)

    dic = {}
    for idx,k in enumerate(room_number) :
        if k not in dic :
            dic[k] = idx+1
            a.remove(k)

        else :
            dic[a[0]] = idx+1
            a.pop(0)

    answer = list(dic.keys())

    return answer

print(solution(10,[1,3,4,1,3,1]))