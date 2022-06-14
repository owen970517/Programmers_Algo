def solution(name):
    answer = 0

    n = 'A'
    for i in name :
        print(i)
        ascii = ord(n)
        for j in range(1,26) :
            ascii +=1
            if chr(ascii) == i :
                answer +=j
    return answer

name = 'JAN'
print(solution(name))