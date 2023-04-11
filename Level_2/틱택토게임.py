def solution(board) :
    answer = -1
    first = 0
    back = 0
    for i in board :
        print(i)
        for j in range(len(list(i))) :
            if i[j] == 'O' :
                first += 1
            elif i[j] == 'X' :
                back += 1
    print(first,back)
    if first + back == 0 :
        answer = 1
    if first > back :
        answer = 1
    if first+back == 6 :
        answer = 0
    else :
        answer = 0 
    return answer
print(solution(["O.X", ".O.", "..X"]))