n = int(input())
li = []
for i in range(n) :
    s = input()
    li.append(s)
li.sort(key=len)
cnt=0
for i in range(n) :
    now = li[i]
    can = False
    for j in range(i+1,n) :
        k = li[j]
        if now == k[0:len(now)] :
            can = True
            break
    if can == False :
        cnt += 1
print(cnt)


























