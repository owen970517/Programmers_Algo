n,c = map(int,input().split())

li = list(map(int,input().split()))
now = li[0]
cnt = 1
for i in range(1,len(li)) :
    if li[i] - now <= c :
        now= li[i]
        cnt += 1
    else :
        now = li[i]
        cnt = 1
print(cnt)