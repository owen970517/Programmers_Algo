def nextPermutation(s):
    k = len(s) - 2
    try:
        k = max(i for (i, x) in enumerate(s[:-1]) if x < s[i+1])
    except ValueError:
        return s
    l = max(k + i for (i, x) in enumerate(s[k:]) if x >= s[k])
    s[k], s[l] = s[l], s[k]
    L = s[:k + 1]
    L.extend(list(reversed(s[k + 1:])))
    return L

n = int(input())
li=[]
for i in range(n) :
    s = list(input())
    target = nextPermutation(s)
    if target :
        li.append(''.join(target))
    else :
        li.append(''.join(s))
for i in li :
    print(i)






# from itertools import permutations

# n = int(input())
# s_li = []
# li = []
# answer = []
# for i in range(n) :
#     s = list(input())
#     s_li.append(''.join(s))
#     nCr = list(set(permutations(s , len(s))))
#     for i in nCr :
#         i = ''.join(i)
#         li.append(i)
#     li.sort()
#     for i in s_li :
#         now_idx = li.index(i)
#         if now_idx == len(li)-1:
#             answer.append(i)
#         else :
#             answer.append(li[now_idx+1])
# set_answer = []
# set_answer.append(answer[0])
# for i in range(1,len(answer)) :
#     if answer[i] not in set_answer :
#         set_answer.append(answer[i])
# for i in set_answer :
#     print(i)



