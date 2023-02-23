n,m = map(int,input().split())
cross_word=[]
li = []
for i in range(n) :
    s = input()
    cross_word.append(s)
for i in cross_word :
    now=''
    for j in range(m) :
        if i[j] =='#' :
            if len(now) <= 1 :
                now=''
                continue
            else :
                break
        else :
            now += i[j]
    if len(now) > 1:
        li.append(now)
for i in range(m) :
    length =''
    for j in range(n) :
        if cross_word[j][i] == '#' :
            if len(length) <= 1 :
                length=''
                continue
            else :
                break
        else :
            length += cross_word[j][i]
    if len(length) > 1 :
        li.append(length)
li.sort()
print(li[0])