from itertools import permutations,combinations

li = []
puzzle = []
for i in range(6) :
    s = input()
    li.append(s)
nPr = list(permutations(li , 3))
for i in nPr :
    now =[]
    for j in i :
        now.append(j)
    print(now)