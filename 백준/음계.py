# 처음에 푼 풀이 (통과)
# li = list(map(int,input().split()))
# isMix = False
# dp = [False] * len(li)
# for i in range(1,len(li)) :
#     if li[i-1] + 1 == li[i]:
#         dp[i-1] = True
#         dp[i] = True
#     elif li[i-1] +1 < li[i] or li[i-1]-1 > li[i] :
#         isMix = True
#         break
# if isMix :
#     print('mixed')
# else :
#     if dp.count(True) == len(li) :
#         print('ascending')
#     else :
#         print('descending')

li = list(map(int,input().split()))
isAsc= False
isDes = False
dp = [False] * len(li)
for i in range(1,len(li)) :
    if li[i] > li[i-1] :
        isAsc = True
    elif li[i] < li[i-1] :
        isDes = True

if isAsc and not isDes:
    print('ascending')
elif isDes and not isAsc:
    print('descending')
else :
    print('mixed')