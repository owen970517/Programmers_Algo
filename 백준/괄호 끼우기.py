s = input()
stack= []
cnt = 0 
for i in range(len(s)) :
    if s[i] == ')' and not stack :
        cnt += 1
    elif stack and s[i] == ')' :
        stack.pop()
    else :
        stack.append(s[i])   
if stack :
    cnt += len(stack)
print(cnt)
