# s = input()
# dic ={}
# li = []
# for i in s :
#     if i not in dic :
#         dic[i] = 1
#     else :
#         dic[i] += 1

# for i in dic :
#     dic[i] //= 2
#     for _ in range(dic[i]) :
#         li.append(i)
# li.sort()
# print(''.join(li))

li = list(input())
zero, one = li.count('0')//2, li.count('1')//2
print(-li[::-1])
for _ in range(zero):
    li.pop(li[::-1].index('0')-1)
for _ in range(one):
    li.pop(li.index('1'))
print(''.join(li))