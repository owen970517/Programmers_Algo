n = int(input())
li = list(map(int,input().split()))
li.sort()
total = 0
print(li)
for i in range(len(li)-1) :
    total += li[i]
print(total)