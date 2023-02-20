s = input()
li=[]
for i in range(len(s)) :
    now = s[:i+1]
    print('지금',now)
    print(s[:i+1])
    print(s[:i+1][-1])
    print(min(s[:i+1]))
    if now[-1] == min(now) :
        mini = now
        print('최소' , mini)
        li.append(mini)
    else :
        s= s[i::]
        print('그다음',s)
print(li)