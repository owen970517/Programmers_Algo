import heapq

# 우선 순위 큐
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

    q = []
    heapq.heappush(q,minutes[0][1]+10)
    room = 1
    for i in range(1,len(minutes)) :
        
        if q and q[0] <= minutes[i][0] :
            heapq.heappop(q)
        else :
            room += 1
        heapq.heappush(q,minutes[i][1]+10)
    answer = len(q)
    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))