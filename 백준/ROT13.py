s = input()
rot = ''
for i in s :
    if i.isalpha() == True and i.islower():
        now = ord(i)+13
        if now > 122 :
            now-=26
        rot += chr(now)
    elif i.isalpha() == True and i.isupper() :
        now = ord(i)+13
        if now > 90 :
            now-=26
        rot += chr(now)
    else :
        rot += i
print(rot)