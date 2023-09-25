from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
d = deque()
for i in range(n) :
    s = list(map(int,input().split()))
    if s[0] == 1 :
        d.appendleft(s[1])
    elif s[0] == 2 :
        d.append(s[1])
    elif s[0] == 3 :
        if len(d) > 0 :
            print(d.popleft())
        else :
            print(-1)
    elif s[0] == 4 :
        if len(d) > 0 :
            print(d.pop())
        else :
            print(-1)
    elif s[0] == 5 :
        print(len(d))
    elif s[0] == 6 :
        if len(d) == 0 :
            print(1)
        else :
            print(0)
    elif s[0] == 7 :
        if len(d) > 0 :
            print(d[0])
        else :
            print(-1)
    elif s[0] == 8 :
        if len(d) > 0 :
            print(d[-1])
        else :
            print(-1)