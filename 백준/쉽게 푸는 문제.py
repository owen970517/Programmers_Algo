a,b = map(int,input().split())
li = []
cnt = 1
while 1 :
    for i in range(cnt) :
        li.append(cnt)
    if len(li) >= b :
        break
    cnt += 1
print(sum(li[a-1:b]))