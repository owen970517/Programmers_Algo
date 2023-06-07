# 시간 초과
# t = int(input())
# for i in range(t) :
#     n = int(input())
#     stock = list(map(int,input().split()))
#     k = max(stock)
#     benefit = 0
#     idx = stock.index(k)
#     for i in range(n-1) :
#         if i > idx  :
#             max_num = max(stock[i:])
#             benefit += max_num - stock[i]
#         else :
#             if k > stock[i] :
#                 benefit += k-stock[i]
#     print(benefit)

t = int(input())
for i in range(t) :
    n = int(input())
    stock = list(map(int,input().split()))
    stock = list(reversed(stock))
    max_num = 0
    benefit = 0
    for j in range(n) :
        if stock[j] > max_num :
            max_num = stock[j]
        else :
            benefit += max_num - stock[j]
    print(benefit)
