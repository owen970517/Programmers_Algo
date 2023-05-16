# 내가 푼 풀이 시간이 3784ms 걸림 

import sys

n = int(sys.stdin.readline())
li =set()
all = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
for i in range(n) :
    s = sys.stdin.readline().strip().split()
    if s[0] == 'add' :
        li.add(int(s[1]))
    elif s[0] == 'remove' :
        li.discard(int(s[1]))
    elif s[0] == 'check' :
        if int(s[1]) in li :
            print(1)
        else :
            print(0)
    elif s[0] == 'toggle' :
        if int(s[1]) in li :
            li.discard(int(s[1]))
        else :
            li.add(int(s[1]))
    elif s[0] == 'all' :
        li = all
        print(li)
    elif s[0] == 'empty' :
        li = set()