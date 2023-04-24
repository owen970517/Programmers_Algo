n = int(input())
cheeses = list(map(str,input().split()))
li = []
for i in cheeses :
    if 'Cheese' in i :
        if i == 'Cheese' :
            li.append(i)
            break
        if i.index('Cheese') == 0 :
            break
        else :
            li.append(i[:i.index('Cheese')])
li = list(set(li))
if len(li) <4 :
    print('sad')
else :
    print('yummy')