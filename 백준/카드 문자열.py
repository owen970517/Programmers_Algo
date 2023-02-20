from collections import deque

t = int(input())
for i in range(t) :
    n = int(input())
    cards = list(map(str, input().split()))
    li = deque()
    li.append(cards[0])
    for i in range(1,len(cards)) :
        first = li[0]
        if cards[i] <= first :
            li.appendleft(cards[i])
        else :
            li.append(cards[i])
    li = list(li)
    print(''.join(li))