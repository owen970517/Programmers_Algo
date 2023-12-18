def k(now) :
    s = ''
    li = []
    for i in now :
        if i == '*' or i =='+' or i =='-' :
            li.append(int(s))
            li.append(i)
            s = ''
        else :
            s += i
    li.append(s)
    return li

a,b = map(str,input().split())
print(max(eval(a),eval(b)))