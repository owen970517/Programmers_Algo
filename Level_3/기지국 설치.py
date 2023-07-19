from math import ceil

def solution(n,stations,w) :
    answer = 0
    li = [i for i in range(1,n+1)]
    w_range = (w*2) + 1
    can = []
    for i in stations :
        k = i-1
        if k== len(li)-1 :
            now = li[k-w:]
        else :
            now = li[k-w:k+w+1]
        can.append(now)


    return answer
# import math

# def solution(n, stations, w):
#     answer = 0
#     range = w + w + 1
    
#     now = 1
#     for station in stations:
#         length = station - w - now
#         if length > 0:
#             answer += math.ceil(length / range)
#         now = station + w + 1
#     print(now)
#     if n >= now:
#         answer += math.ceil((n - now + 1) / range)

#     return answer
print(solution(11,[4,11],1))