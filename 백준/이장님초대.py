# 내가 푼 풀이 (시간초과)
# n = int(input())
# seeds = list(map(int,input().split()))
# seeds.sort(reverse=True)
# day = 0
# if len(seeds) == 1 :
#     print(seeds[0] + 2)
# else :
#     for i in range(len(seeds)) :
#         day += 1
#         for j in range(i) :
#             seeds[j] -= 1
# print(day + max(seeds) + 1)

# 대중적인 풀이
n = int(input())
seeds = list(map(int,input().split()))
seeds.sort(reverse=True)
li = []
if len(seeds) == 1 :
    print(seeds[0] + 2)
else :
    for i in range(len(seeds)) :
        li.append(seeds[i] + 1 + i)
    print(max(li) + 1)