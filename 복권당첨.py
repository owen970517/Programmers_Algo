def solution(lotteries) :
    answer = []
    per_li = []
    price_list = []
    for i in range(len(lotteries)) :
        winner= lotteries[i][0]
        buyer = lotteries[i][1]
        if (buyer < winner) :
            per = 100
        else :
            per = (winner / (buyer+1)) * 100
        per_li.append(per)
        price_list.append(lotteries[i][2])
    now = per_li[0]
    now_price = price_list[0]
    for i in range(1,len(per_li)) :
        if now > per_li[i] :
            continue
        elif now == per_li[i] :
            if now_price < price_list[i] :
                now = per_li[i]
                now_price = price_list[i]
        else :
            now = per_li[i]
            now_price = price_list[i]
    print(now,now_price)
    answer.append(price_list.index(now_price)+1)
 

    return answer,per_li,price_list

print(solution([[100,100,500],[1000,1000,100]]))
#100,100,500 1000,1000,100
#10 19 800 20 39 200 100 199 500
#[50,1,50],[100,199,100],[1,1,500]