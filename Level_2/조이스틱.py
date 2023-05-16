def solution(name):
    answer = 0
    print(name.find('A'))
    now = 'A' * len(name)
    last = 'Z'
    for idx,k in enumerate(name) :
        print(k)
        answer += min(ord(k) - ord('A'), ord('Z') - ord(k) + 1)

    return answer

name = 'JAN'
print(solution(name))