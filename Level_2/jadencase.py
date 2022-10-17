def solution(s):
    answer = ''
    s=s.split(' ')
    array = []
    for i in s:
        if s[0].isdigit() :
            array.append(i)
        else :
            array.append(i.capitalize())
    answer=' '.join(array)
    return answer

print(solution("3people unFollowed me"))