n = list(input())
ans =''
for i in n :
    if i.isupper() :
        i=i.lower()
        ans += i
    else :
        i=i.upper()
        ans += i

print(ans)