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
# s = ''
# li = []
# for i in a :
#     if i == '*' or i =='+' or i =='-' :
#         li.append(s)
#         li.append(i)
#         s = ''
#     else :
#         s += i

print(k(a))
print(k(b))

a,b = map(str,input().split())
print(max(eval(a),eval(b)))