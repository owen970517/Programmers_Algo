#처음 푼 방법 
# 매번 새로운 리스트를 생성하고, sum() 하기 때문에 메모리초과가 발생 
# n = int(input())
# li = [i for i in range(1,n+1)]
# start = 0
# end =0 
# ans =0 
# while start <= n and end <= n :
#     now = li[start:end+1]   
#     if sum(now) == n :
#         ans += 1
#         start += 1
#         end = start
#     else :
#         if sum(now) < n :
#             end += 1
#         else :
#             start += 1
#             end = start
# print(ans)


# 찾아보고 해결한 풀이 
n = int(input())
start = 1
end = 1
total = 0
total += start
ans = 0

while start <= n:
    if total == n:
        ans += 1
        total -= start
        start += 1
    else :
        if total < n:
            end += 1
            total += end
        else:
            total -= start
            start += 1
print(ans)