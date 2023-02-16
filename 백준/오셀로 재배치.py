k = int(input())
answer = []
for _ in range(k) :
    change=[]
    cnt = 0
    n = int(input())
    init = list(input())
    goal = list(input())
    print(init,goal)
    for i in range(n) :
        if init[i] != goal[i] :
            change.append(init[i])
    print(change)
    if change.count('B') >= change.count('W') :
        cnt = change.count('B')
    else :
        cnt = change.count('W')
    answer.append(cnt)
for i in answer :
    print(i)
