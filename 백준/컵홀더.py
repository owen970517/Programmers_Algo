from collections import deque

n = int(input())
seat = input()
li = deque()
couple = ''
cnt = 0

for i in range(len(seat)) :
    if i == 0 :
        li.appendleft('*')
        cnt += 1
    if seat[i] == 'S' :
        li.append(seat[i])
        li.append('*')
        cnt += 1
    if i == len(seat) :
        li.append('*')
        cnt += 1
    else :
        if seat[i] == 'L' :
            couple += seat[i]
            if couple == 'LL' :
                li.append(couple)
                li.append('*')
                cnt += 1
                couple =''
if cnt > n :
    print(n)
else :
    print(cnt)