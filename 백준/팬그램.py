n = int(input())
for i in range(n) :
    s = list(input().split())
    dic = {
    'a':0,
    'b' :0,
    'c':0,
    'd' : 0,
    'e' :0,
    'f' : 0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p' :0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0
}
    for j in s :
        j = j.lower()
        for k in range(len(j)) :
            if j[k] in dic :
                dic[j[k]] +=1
    if min(dic.values()) == 0:
        print(f'Case {i+1}: Not a pangram')
    elif min(dic.values()) == 1:
        print(f'Case {i+1}: Pangram!')
    elif min(dic.values()) == 2:
        print(f'Case {i+1}: Double pangram!!')
    elif min(dic.values()) == 3:
        print(f'Case {i+1}: Triple pangram!!!')


