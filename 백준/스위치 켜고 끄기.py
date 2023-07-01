n = int(input())
li = list(map(int,input().split()))
t = int(input())
for i in range(t) :
    gender,num = map(int,input().split())
    if gender == 1 :
        for j in range(len(li)) :
            if (j+1) % num == 0 :
                if li[j] == 0 :
                    li[j] = 1
                else :
                    li[j] = 0
    if gender == 2 :
        now=num-1
        cnt = 1
        if li[now] == 0:
            li[now] = 1
        else :
            li[now] = 0 
        while 1 :
            if now-cnt<0 or now+cnt > len(li)-1 :
                break
            if li[now-cnt] == li[now+cnt] :
                if li[now-cnt] == 0 and li[now+cnt] == 0 :
                    li[now-cnt],li[now+cnt] = 1,1
                else :
                    li[now-cnt],li[now+cnt] = 0,0
            else :
                break
            cnt+= 1
for i in range(n) :
    print(li[i], end=' ')
    if i % 20 == 19 :
        print()
