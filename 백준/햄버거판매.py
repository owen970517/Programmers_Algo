n,m = map(int,input().split())
li = list(input())
cnt = 0
for i in range(len(li)) :
    if li[i] == 'P' :
        for j in range(i-m, i+m+1): 
            if 0 <= j < n and li[j] == "H": 
                cnt += 1
                li[j] = 0
                break 
print(cnt)

# 내가 푼 풀이
# n,m = map(int,input().split())
# li = list(input())
# cnt = 0
# for i in range(len(li)) :
#     if li[i] == 'P' :
#         # for j in range(1,m+1) :
#         #     if i-m > 0 and li[i-m] =='H' :
#         #         cnt += 1
#         #         li[i-m] = 0
#         #         break
#         #     elif i+j < len(li) and li[i+j] == 'H' :
#         #         cnt += 1
#         #         li[i+j] = 0
#         #         break
# print(cnt)

