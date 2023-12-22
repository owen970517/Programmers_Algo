# s = input()
# li=[]
# now = ''
# if s.find('<') == -1 :
#     s = s.split(' ')
#     for i in s :
#         li.append(i[::-1]+' ')
# else :
#     for i in range(len(s)) :
#         if s[i] == '<' and len(now) != 0 :
#             li.append(now[::-1])
#             now = ''
#             now += s[i]
#         elif s[i] == '>' :
#             now += s[i]
#             li.append(now)
#             now=''
#         elif now.find('<') == -1 and s[i] ==' ' :
#             li.append(now[::-1]+s[i])
#             now =''
#         else :
#             now += s[i]
#     li.append(now[::-1])
# print(''.join(li))
t = int(input())

for i in range(t) :
    li = []
    s = input().split()
    for k in s :
        li.append(k[::-1])
    print(' '.join(li))