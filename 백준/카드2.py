from collections import deque

n = int(input())
li = deque()
for i in range(n) :
    li.append(i+1)
while 1 :
    if len(li) == 1 :
        break
    li.popleft()
    li.append(li.popleft())
print(li[0])
