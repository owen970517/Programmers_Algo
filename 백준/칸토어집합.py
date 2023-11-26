# def cantor(start,mid,end) :
#     if len(start) == 1 and len(mid) == 1 and len(end) == 1:
#         return ''.join(start)+' '+''.join(mid)+' '+''.join(end)
#     else :
#         start = start[:len(start)//3]
#         for i in range(len(mid)) :
#             mid[i] = ' '
#         end = end[len(end)*2::]
#         return cantor()
def solution(now) :
    start = now[:len(now)//3]
    mid = now[len(now)//3:len(now)//3*2]
    end = now[len(now)//3*2::]
    if len(start) == 1 and len(mid) == 1 and len(end) == 1:
        return now
    else:
        for i in range(len(mid)) :
            mid[i] = ' '
        return solution(start) + solution(mid) + solution(end)
n = int(input())
now = ['-'] * (3**n)
total = 3**n

print(solution(now))
