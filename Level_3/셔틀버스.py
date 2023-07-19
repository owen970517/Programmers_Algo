def solution(n,t,m,timetable) :
    answer = ''
    start = '09:00'
    cnt = 0 
    print(start > timetable[2])
    timetable.sort()
    print(timetable)
    if m < len(timetable) :
        for i in range(m) :
            if timetable[i] <= start :
                timetable.pop(i)
        cnt+=1 
    
    print(timetable)
    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))