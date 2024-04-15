# 61%에서 시간초과 발생 
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
S = set()
ans = 0
for _ in range(n) :
    now = input().rstrip()
    for i in range(1, len(now) + 1):
        S.add(now[:i])
print(S)
for _ in range(m) :
    k = input().rstrip()
    if k in S :
        ans += 1

print(ans)
# 61퍼에서 시간초과
# n,m = map(int,input().split())
# S = []
# ans = 0
# for _ in range(n) :
#     now = input()
#     S.append(now)

# for _ in range(m) :
#     k = input()
#     for i in S :
#         if k[0] == i[0] :
#             if k == i[:len(k)] :
#                 ans += 1
#                 break
# print(ans)