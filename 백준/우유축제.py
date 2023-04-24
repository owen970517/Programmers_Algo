n = int(input())
shops = list(map(int,input().split()))
cnt = 0
milk = []
for i in range(len(shops)) :
    if cnt ==0 :
        if shops[i] == 0 :
            cnt += 1
            milk.append(shops[i])
    else :
        if milk[-1] == 0 :
            if shops[i] == 1 :
                cnt += 1
                milk.append(shops[i])
        elif milk[-1] == 1 :
            if shops[i] == 2 :
                cnt += 1
                milk.append(shops[i])
        elif milk[-1] == 2 :
            if shops[i] == 0 :
                cnt += 1
                milk.append(shops[i])
print(cnt)