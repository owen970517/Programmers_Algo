n = int(input())
li = set()
for i in range(n):
    a,b = map(str,input().split())
    if b == 'enter' :
        li.add(a)
    if b == 'leave' :
        li.remove(a)
li = list(li)
li.sort(reverse=True)
for i in li :
    print(i)