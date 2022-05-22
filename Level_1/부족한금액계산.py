def solution(price, money, count):
    answer = 0
    n=1
    while n <= count:
        answer +=price*n
        n+=1
    if answer > money :
        answer -=money
    else:
        answer = 0
    return answer

price = 3
money = 20
count=4
print(solution(price,money,count))