from collections import deque

t = int(input())
for i in range(t) :
    n,m = map(int,input().split())    
    li = deque(map(int,input().split()))
    rank = 0
    while li :
        maximum = max(li)
        first = li.popleft()
        m-=1
        if maximum == first :
            rank += 1
            if m <= 0 :
                print(rank)
                break
        else :
            li.append(first)
            if m < 0 :
                m = len(li)-1


# answer = deque([1,1,9,1,1,1])
# for i in range(4) :
#     for j in range(1,4) :
#         print(answer)
#         if answer[0] < answer[j] :
#             now = answer.popleft()
#             answer.append(now)
#             break