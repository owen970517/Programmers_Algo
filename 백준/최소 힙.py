import heapq
import sys 

input = sys.stdin.readline
n = int(input())
li = []
for i in range(n) :
    s=int(input())
    if s == 0 :
        if len(li) > 0 :
            print(heapq.heappop(li))
        else :
            print(0)
    else :
        heapq.heappush(li,s)