li=[]
for _ in range(9):
    k = int(input())
    li.append(k)
total = sum(li)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if total-(li[i] + li[j])==100:
            first = li[i]
            second = li[j]
            break
li.remove(first)
li.remove(second)
li.sort()
for i in li:
    print(i)