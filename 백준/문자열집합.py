n,m = map(int,input().split())
s = []
li = []
cnt = 0
for i in range(n+m) :
    now =input()
    if i <n :
        s.append(now)
    else :
        li.append(now)
for i in li :
    if i in s :
        cnt += 1
print(cnt)