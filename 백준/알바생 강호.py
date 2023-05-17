import sys
input = sys.stdin.readline

n = int(input())
li = []
total = 0
for i in range(n) :
    tip = int(input())
    li.append(tip)

li.sort(reverse=True)
for i in range(len(li)) :
    now = li[i] - ((i+1)-1)
    if now <= 0 :
        break
    total += now
print(total)