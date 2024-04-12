import sys

input=sys.stdin.readline
t = int(input().rstrip())
for _ in range(t) :
    n = int(input().rstrip())
    li = []
    for _ in range(n) :
        phone = input().rstrip()
        li.append(phone)
    li.sort()
    isConsistency = True
    for i in range(len(li)-1) :
        if li[i] == li[i+1][:len(li[i])] :
            isConsistency = False 
            break
    if isConsistency :
        print('YES')
    else :
        print('NO')
