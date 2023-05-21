while 1 :
    dic = {
        ')' : '(',
        ']' : '['
    }
    s = input()
    stack = []
    if s == '.' :
        break
    for i in s :
        if i == '(' or i =='[':
            stack.append(i)
        elif i ==')' or i ==']' :
            if stack and stack[-1] == dic[i] :
                stack.pop()
            else :
                stack.append(i)
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')