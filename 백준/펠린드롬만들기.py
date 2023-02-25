s = input()
now = ''
for i in range(len(s)) :
    if s[i:] == s[i:][::-1] :
        now += s[:i]
        break
if len(now) > 0 :
    s += now[::-1] 
    print(len(s))
else :
    print(len(s))