li = []
for i in range(5) :
    k = int(input())
    li.append(k)

li.sort()
print(sum(li)//5)
print(li[2])