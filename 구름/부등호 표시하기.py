li = list(map(int,input().split()))
s = ''
s += str(li[0])
for i in range(2) :
    if li[i] > li[i+1] :
        s += '>'
        s +=str(li[i+1])
    elif  li[i] == li[i+1] :
        s += '=='
        s += str(li[i+1])
    else :
        s +='<'
        s +=str(li[i+1])
print(s)
