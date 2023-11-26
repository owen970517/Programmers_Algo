li = []
total = 0 
for i in range(3) :
    n = int(input())
    total += n
    if n not in li :
        li.append(n)
print(total,li)
if total == 180 :
    if len(li) == 3 :
        print('Scalene')
    elif len(li) == 2 :
        print('Isosceles')
    else :
        print('Equilateral')
else :
    print('Error')