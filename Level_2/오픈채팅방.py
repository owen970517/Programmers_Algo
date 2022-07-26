def solution(record):
    answer = []
    dic ={}
    for i in record :
        li = i.split(' ')
        if li[0] == 'Enter' :
            dic[li[1]] = li[2]
        elif li[0] == 'Change' :
            dic[li[1]] = li[2]
    for i in record :
        li = i.split(' ')
        if li[0] == 'Enter' :
            answer.append(f'{dic[li[1]]}님이 들어왔습니다.')
        elif li[0] == 'Leave' :
            answer.append(f'{dic[li[1]]}님이 나갔습니다.')

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))

"""     for i in record:
        li=i.split()
        if len(li) == 3 : 
            dic[li[1]] = li[2]
    for i in record :
        li = i.split()
        if li[0] == 'Enter' :
            answer.append('%s님이 들어왔습니다.' %dic[li[1]])
        elif li[0] =='Leave':
            answer.append('%s님이 나갔습니다.' %dic[li[1]]) """