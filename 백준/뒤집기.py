s = input()
li =[]
now =s[0]
cnt =0
one = 0
zero = 0
for i in range(1,len(s)) :
    if now[-1] == s[i] :
        now +=s[i]
    else :
        li.append(now)
        now = s[i]
li.append(now)
for i in li :
    if i.find('1') == -1 :
        zero += 1
    else :
        one += 1
if zero < one :
    print(zero)
else :
    print(one)