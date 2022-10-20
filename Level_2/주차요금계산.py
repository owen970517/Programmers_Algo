import math
def solution(fees, records):
    answer = []
    parking = {}
    stack = {}
    
    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute) 
        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car]
    for i,minute in parking.items() :
        if len(parking) :
            stack[i] += 23*60 + 59 - minute  
        else :
            stack[i] = 23*60+59 - minute
    stack = dict(sorted(stack.items(), key=lambda x: x[0]))
    for i in stack:
        cost = 0 
        if stack[i] < fees[0] :
            cost = fees[1]
        else :
            cost = math.ceil((stack[i]-fees[0])/fees[2])*fees[3] + fees[1]
        answer.append(cost)    
    return answer

print(solution([180, 5000, 10, 600] , ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))