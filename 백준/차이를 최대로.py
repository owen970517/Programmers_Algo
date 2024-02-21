from itertools import permutations

n = int(input())
li = list(map(int,input().split()))
nPr = list(permutations(li,n))

ans = 0
for i in nPr :
    now = 0
    for j in range(n-1) :
        now += abs(i[j]-i[j+1])
    ans = max(ans,now)

print(ans)


# from itertools import permutations
# import sys
 
# # 주어진 값 입력
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
 
# # permutation 저장(per: reference of permutation tuples)
# per = permutations(a)
# ans = 0
 
# # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
# for i in per:
#     s = 0
#     for j in range(len(i)-1):
#         s += abs(i[j]-i[j+1])
#     if s > ans:
#         ans = s
 
# print(ans)