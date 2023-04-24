# 내가 푼 풀이
# n = int(input())
# prices = []
# total = 0
# for i in range(n) :
#     p = int(input())
#     prices.append(p)
# prices.sort(reverse=True)
# prices = [prices[i:i+3] for i in range(0, len(prices), 3)]
# for i in prices :
#     if len(i) == 3 :
#         total += sum(i[:2])
#     else :
#         total += sum(i)
# print(total)

#다른 사람 풀이
n = int(input())
prices = []
total = 0
for i in range(n) :
    p = int(input())
    prices.append(p)
prices.sort(reverse=True)
for i in range(len(prices)) :
    if i % 3 != 2 :
        total += prices[i]
print(total)