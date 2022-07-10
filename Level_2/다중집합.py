a = [1, 1, 2, 2, 3]
b = [1, 2, 2, 4, 5]

a1 = a.copy()
a2 = a.copy()
anb=[]
for i in b :
    if i not in a1:
        a2.append(i)
    else :
        a1.remove(i) 

for i in b :
    if i in a :
        anb.append(i)

print(a2)
print(anb)