n,m = map(int,input().split())
j = int(input())
screen = []
cnt = 0
for i in range(n) :
    screen.append(i+1)
basket = screen[:m]
for i in range(j) :
    apple = int(input())
    if apple in basket :
        continue
    else :
        while 1 :
            if apple in basket :
                break
            for i in range(len(basket)) :
                if basket[i] < apple :
                    basket[i] += 1
                else :
                    basket[i] -= 1
            cnt += 1
print(cnt)
