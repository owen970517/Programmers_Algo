li=[]
while 1 :
    cnt = 0
    stack = []
    s = input()
    li.append(s)
    if s.find('-') == 0 :
        break
    for i in range(len(s)) :
        if s[i] == '}' and not stack :
            cnt += 1
            stack.append('{')
        elif stack and s[i] == '}' :
            print(stack.pop())
        else :
            stack.append(s[i])
    cnt += len(stack) // 2
    print(f'{len(li)}. {cnt}')
# li=[]
# while 1 :
#     match = {
#         '}': '{',
#     }
#     cnt = 0
#     stack = []
#     s = input()
#     if s.find('-') == 0 :
#         break
#     for i in range(len(s)) :
#         if s[i] in match and len(stack) == 0 :
#             cnt += 1
#             stack.append(match[s[i]])
#         elif len(stack) > 0 and stack.pop() == s[i] :
#             cnt += 1
#         else :
#             stack.append(s[i])
#     li.append(cnt)
# for i in range(len(li)) :
#     print(f'{i+1}. {li[i]}')



