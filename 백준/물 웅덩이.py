n,l = map(int,input().split())
li =[]
length = 0
ans = 0
for i in range(n) :
    s= list(map(int,input().split()))
    li.append(s)
li.sort(key=lambda x:x[0])
pool = li[0][0]
print(li)
for s,e in li :
    if pool > e :
        continue
    elif pool < s :
        pool = s
    length = e-pool
    cnt = 1
    if length % l == 0 :
        cnt = 0
    now = length // l + cnt
    pool += now * l
    ans += now
print(ans)
        
