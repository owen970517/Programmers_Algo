def solution(today,term,privacies) :
    answer = []
    li=[]
    for i in privacies :
        i = i.split(' ')
        privacy = i[0].split('.')
        for j in term :
            k= ''
            j = j.split(' ')
            if j[0] == i[1] :
                year = int(privacy[0])
                month= int(privacy[1]) + int(j[1])
                day = int(privacy[2])
                if month <= 12 :
                    if day == 1 :
                        day = 28
                        month -= 1
                    if month == 1 :
                        year -= 1
                        month = 12
                    else :
                        day -= 1
                else :
                    year += month//12
                    month = month % 12
                    if month ==0 :
                        year -= 1
                        month = 12
                    if day == 1 :
                        month -= 1
                        day = 28
                    else :
                        day -= 1
                month = str(month).zfill(2)
                day = str(day).zfill(2)
                k = str(year) + month + day
                li.append(int(k))
    today = int(today.replace('.',''))
    
    for i in range(len(li)) :
        if li[i]+1 <= today :
            answer.append(i+1)
    return answer

print(solution("2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"]))