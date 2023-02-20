from itertools import combinations,permutations,product

syllable = ['pi','ka','chu']
s = input()
can =True
for i in syllable :
    if i in s :
        s=s.replace(i,'*')
for i in s :
    if i != '*' :
        can = False
if can :
    print('YES')
else :
    print('NO')


# li=[]
# nCr = list(product(syllable,repeat=3))
# for i in nCr :
#     now = i[0]+i[1]+i[2]
#     li.append(now)
# print(li)
# if s not in li :
#     print('NO')
# else :
#     print('YES')