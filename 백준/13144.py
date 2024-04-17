# 1번째 내가 푼 방법= 시간초과 
# n = int(input())
# li = list(map(int,input().split()))
# ans = 0

# for i in range(len(li)) :
#     start,end = i,i
#     while end < len(li) :
#         now = li[start:end+1]
#         if len(now) == len(set(now)) :
#             ans += 1
#         end += 1
# print(ans)

# 2번째 내가 푼 방법 = 시간초과 
# n = int(input())
# li = list(map(int,input().split()))
# ans = 0
# start,end = 0,0

# while 1 :
#     if start == end == len(li)-1:
#         ans += 1
#         break
#     now = li[start:end+1]
#     if len(now) == len(set(now)) :
#         ans += 1
#         end += 1
#         if end == len(li) :
#             start += 1
#             end = start
#     else :
#         start += 1
#         end = start
# print(ans)

# 다른 사람 풀이 
n = int(input())
li = list(map(int, input().split()))
ans = 0
start = 0
end = 0
used = set()

while end < n:
    if li[end] not in used:
        used.add(li[end])
        ans += (end - start + 1) 
        end += 1
    else:
        used.remove(li[start])
        start += 1

print(ans)
