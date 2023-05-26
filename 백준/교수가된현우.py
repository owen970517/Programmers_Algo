import sys

input = sys.stdin.readline

t=int(input())
for i in range(t) :
    k = int(input())
    cnt = 0
    n=5 
    while n <= k :
        cnt += k//n
        n*= 5
    print(cnt)