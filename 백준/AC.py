# R이 나올때마다 뒤집으면 시간 초과 발생 
# R이 짝수냐 홀수냐에 따라 뒤집을지 안뒤집을지 정함

from collections import deque
import sys

input = sys.stdin.readline
t = int(input())
for i in range(t) :
    isError = False
    cmd = list(input().strip())
    n = int(input())
    li = deque(input().strip()[1:-1].split(',')) 
    R_count = 0
    if n == 0 :
        li = []
    for now in cmd :
        if now =='R' :
            R_count += 1
        if now == 'D' :
            if len(li) > 0 :
                if R_count % 2 == 0 :
                    li.popleft()
                else :
                    li.pop()
            else :
                isError = True
                print('error')
                break
    if not isError :
        if R_count % 2 == 1 :
            li.reverse()
        print('['+','.join(li)+']')
    # if len(li) > 2 :
    #     li= list(map(int,li.replace('[','').replace(']','').split(',')))
    # else :
    #     print('error')
    #     continue
    # while cmd :
    #     now = cmd.popleft()
    #     if now == 'R' :
    #         li = li[::-1]
    #     if now == 'D' :
    #         if len(li) > 0 :
    #             li.pop(0)
    #         else :
    #             isError = True
    #             break
    #     print(li)
    # if isError :
    #     print('error')
    # else :
    #     print(li)
