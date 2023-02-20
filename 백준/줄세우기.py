n = int(input())
li=[]
for i in range(n) :
    s = input()
    li.append(s)

de = sorted(li,reverse=True)
inc = sorted(li)
if li == de :
    print('DECREASING')
elif li == inc :
    print('INCREASING')
else :
    print('NEITHER')
