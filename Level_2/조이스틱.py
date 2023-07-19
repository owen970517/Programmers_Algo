def solution(name):
    answer = 0
    min_ = len(name)-1
    for idx,k in enumerate(name) :
        answer += min(ord(k)-ord('A'),ord('Z')-ord(k)+1)
        next_ = idx+1
        while next_ < len(name) and name[next_] == 'A':
            next_ += 1
        min_ = min(min_ , idx + len(name)-next_ + min(idx,len(name)-next_))
    answer += min_

    return answer

name = 'JAN'
print(solution(name))