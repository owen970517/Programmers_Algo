def setMinutes(time) :
    entrance = int(time[0].split(':')[0])* 60 + int(time[0].split(':')[1])
    leave = int(time[1].split(':')[0])* 60 + int(time[1].split(':')[1])
    return [entrance,leave]

def solution(book_time) :
    answer = 0
    minutes = []
    book_time.sort(key=lambda x:(x[0],x[1]))
    for i in book_time :
        minutes.append(setMinutes(i))
    for i in range(1,len(minutes)) :
        print(i,i-1)

    return answer,book_time,minutes

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))