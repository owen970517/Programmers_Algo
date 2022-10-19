def solution(s):
    answer = []
    s= s.replace('{{' ,'').replace('}}' ,'')
    s=s.split('},{')
    s.sort(key=len)
    for i in s :
        k = i.split(',')
        for j in k :
            if int(j) not in answer :
                answer.append(int(j))
  
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
