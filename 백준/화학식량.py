s = input()
dic = {
    'H' : 1,
    'C' : 12,
    'O' : 16
}
stack = []
atom = ''
li = []
no_li = []
sum = 0
for i in range(len(s)) :
    if s[i] == '(' :
        stack.append(s[i])
        if atom:
            print(atom)
            li.append(atom)
            atom=''
    elif stack and s[i] ==')' :
        stack.pop()
        if atom:
            li.append(atom)
            atom=''
    else :
        atom += s[i]
        if i ==len(s)-1 :
            li.append(s[i])

print(li)
for i in range(len(li)):
    if li[i].isdigit() :
        sum*=int(li[i])
    else :
        if len(li[i]) == 1 :
            sum += dic[li[i]]
        else :
            now = 0
            for k in range(len(li[i])) :
                if li[i][k].isdigit() :
                    now +=dic[li[i][k-1]] * int(li[i][k])
                    now -= dic[li[i][k-1]]
                else :
                    print(dic[li[i][k]])
                    now += dic[li[i][k]]
            sum += now

print(sum)


# s = input()

# d = {
#     "H" : 1,
#     "C" : 12,
#     "O" : 16
# }

# stack = []

# for i in s:
#     if i in d:
#         stack.append(d[i])
#     elif i == "(":
#         stack.append(i)
#     elif i == ")":
#         temp = 0
#         while True:
#             p = stack.pop()

#             if p == "(":
#                 break

#             temp += p
        
#         if temp == 0:
#             continue
#         else:
#             stack.append(temp)
#     else:
#         n = stack.pop()
#         temp = n*int(i)
#         stack.append(temp)

# print(sum(stack))