n = int(input())
li = []
total = 0
cnt = 0
while 1 :
    if total == n :
        break
    else :
        now = 2 ** cnt
        if now > (n-total) :
            total += (2**(cnt-1))
            li.append(cnt-1)
            cnt = 0
        else :
            cnt += 1
li.sort()
print(len(li))
print(*li)
