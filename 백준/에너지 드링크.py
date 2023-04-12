n = int(input())
li = list(map(int,input().split()))
li = sorted(li)
while len(li) :
    if len(li) == 1 :
        break
    li[-1] += li.pop(0)/2
print(li[0])