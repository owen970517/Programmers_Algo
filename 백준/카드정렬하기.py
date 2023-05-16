import heapq

n= int(input())
li = []
for i in range(n) :
    s = int(input())
    heapq.heappush(li,s)
if len(li) == 1 :
    print(0)
else :
    total = 0
    while len(li) > 1 :
        prev = heapq.heappop(li)
        now = heapq.heappop(li)
        total += prev+now
        heapq.heappush(li,prev+now)
    print(total)