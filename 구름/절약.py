n = int(input())
total = 0
isSave = True
for i in range(n) :
    c,v = input().split()
    v = int(v)
    if c == 'in' :
        total += v
    else :
        if v > total :
            isSave = False
        else :
            total -= v
if isSave :
    print('success')
else :
    print('fail')