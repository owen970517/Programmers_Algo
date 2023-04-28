n = int(input())
li = []
for _ in range(n) :
    R,G,B = map(int,input().split())
    li.append([R,G,B])
sum = min(li[0])
now_idx = li[0].index(min(li[0]))
print(now_idx)
for i in range(1,len(li)) :
    if now_idx == 0 :
        new_li = li[now_idx+1:]
        
print(sum)
