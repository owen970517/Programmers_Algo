cash = int(input())
stock = list(map(int,input().split()))

sungmin =0
sungmin_money = cash
junhyun = 0
junhyun_money = cash
for i in stock :
    if junhyun_money >= i :
        junhyun += (junhyun_money // i)
        junhyun_money %= i
increase= 0
decrease = 0
for i in range(1,len(stock)-1) :
    if stock[i-1] > stock[i] :
        decrease += 1
        increase = 0
        if decrease >= 3  :
            sungmin += (sungmin_money // stock[i])
            sungmin_money%= stock[i]
    elif stock[i] > stock[i-1] :
        increase += 1
        decrease = 0
        if sungmin >0 and increase >= 3 :
            sungmin_money += (sungmin * stock[i])
            sungmin = 0
sungmin = sungmin_money + (sungmin * stock[-1])
junhyun = junhyun_money + (junhyun * stock[-1])
if sungmin > junhyun : 
    print('TIMING')
elif junhyun > sungmin : 
    print('BNP')
else :
    print("SAMESAME")
    

