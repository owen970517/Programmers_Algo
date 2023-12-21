# 미리 1~20까지의 집합을 만들어놓고 all시 할당한 부분이 틀렸었음 

import sys

n = int(sys.stdin.readline())
li =set()
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
        li = set([i for i in range(1, 21)])
    elif s[0] == 'empty' :
        li = set()