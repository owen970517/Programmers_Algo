def solution(plans) :
    answer = []
    dic = dict()
    plans.sort(key=lambda x : x[1])
    for i in plans :
        h,m = map(int,i[1].split(':'))
        i[1] = h*60 + m
        i[2] = int(i[2])
    now = plans.pop(0)
    stop = []
    while 1 :
        if plans :
            if now[1] + now[2] > plans[0][1] :
                remain = now[2] - (plans[0][1]-now[1])
                dic[now[0]] = remain
                stop.append(now)
                if plans :
                    now = plans.pop(0)
                now=now
                print(plans)
            else :
                answer.append(now[0])
                now_time = now[1] + now[2]
                print(now_time,stop)
                if stop :
                    now = stop.pop()
                    now[1] = now_time
                    now[2] = dic[now[0]]
                    print(now,plans[0])
                else :
                    now = plans.pop(0)
                    print(now)
        else :
            answer.append(now[0])
            for i in range(len(stop)) :
                answer.append(stop.pop()[0])
            break
    return answer


print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))

# 다른 사람의 풀이 
# def solution(plans):
#     plans.sort(key = lambda x: x[1])
#     answer = []
#     stack = []

#     for subject, start, time in plans:
#         h, m = map(int, start.split(':'))
#         start = 60*h+m
#         time = int(time)
#         print(stack)
#         if stack:
#             prev_subject, prev_start, playTime = stack.pop()
#             dis_time = start - prev_start
#             print(dis_time)
#             if prev_start+playTime > start:
#                 stack.append((prev_subject, prev_start, playTime-dis_time))
#             else:
#                 answer.append(prev_subject)
#                 dis_time = dis_time - playTime
#                 while stack and dis_time :
#                     prev_subject, prev_start, playTime = stack.pop()

#                     if dis_time < playTime:
#                         stack.append((prev_subject, prev_start, playTime-dis_time))
#                         break
#                     else:
#                         answer.append(prev_subject)
#                         dis_time = dis_time - playTime

#         stack.append((subject, start, time))

#     answer.extend([s for s, _, _ in stack[::-1]])

#     return answer