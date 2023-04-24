str='AbCd'
new =''
for i in str :
    print(i.isupper())
    if i.isupper() :
        i = i.lower()
    else :
        i=i.upper()
    new += i
print(str,new)