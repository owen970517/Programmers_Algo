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
        new_li = li[i][now_idx+1:]
        print(new_li)
        now_idx = new_li.index(min(new_li))
        print(now_idx,new_li[now_idx])
        sum += min(new_li)
    elif now_idx == 2 :
        new_li = li[i][:now_idx]
        print(new_li)
        now_idx = new_li.index(min(new_li))
        print(now_idx,new_li[now_idx])
        sum += min(new_li)
    elif now_idx == 1 :
        new_li = li[i][:now_idx] + li[i][now_idx+1:]
        print(new_li)
        now_idx = new_li.index(min(new_li))
        print(now_idx,new_li[now_idx])
        sum += min(new_li)
print(sum)
