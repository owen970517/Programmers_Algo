# n = int(input())
# answer = 0
# li = []
# dic = dict()
# for i in range(n) :
#     s = input()
#     if i == 0 :
#         for i in range(len(s)) :
#             if s[i] in dic :
#                 dic[s[i]] += 1
#             else :
#                 dic[s[i]] = 1
#     li.append(s)
# print(li,dic)
# # dic['L'] =dic.pop('O')
# print(dic.get())
# for i in range(1,len(li)) :
#     new_dic = {}
#     for j in range(len(li[i])) :
#         if li[i][j] in new_dic :
#             new_dic[li[i][j]] += 1
#         else :
#             new_dic[li[i][j]] = 1
#     if dic == new_dic :
#         answer += 1
#     else :
#         for i in dic :
#             if i in new_dic and dic[i] < new_dic[i] :
#                 dic[i] += 1
#                 if dic == new_dic :
#                     answer +=1
#                     break
#                 else :
#                     dic[i] -= 1
#             elif i in new_dic and dic[i] > new_dic[i] :
#                 dic[i] -= 1
#                 if dic == new_dic :
#                     answer += 1
#                     break
#                 else :
#                     dic[i] += 1
#             elif i not in new_dic :
#                 dic[]

# print(answer)

N = int(input())
answer = 0
li = []
cnt = 0
for i in range(N):
    s = input() # 새로운 단어
    li.append(s)
print(li)
for i in range(1,len(li)):
    target = list(li[0])
    print(li[i],target)
    for j in li[i] :
        if j in target :
            target.remove(j)
            print(target)
        else :
            cnt += 1
    if cnt <2 and len(target) <2 :
        answer += 1
# n = int(input())
# target = list(input()) 
# answer = 0

# for _ in range(n-1):
#     compare = target[:]
#     print(compare)
#     word = input() 
#     cnt = 0

#     for w in word:
#         if w in compare:
#             compare.remove(w)
#         else:
#             cnt += 1

#     if cnt < 2 and len(compare) < 2:
#         answer += 1
#     print(target)
print(answer)
