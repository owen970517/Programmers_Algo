n = int(input())
cnt = 0
for i in range(n) :
    stack =[]
    s = input()
    for j in s :
        if not stack :
            stack.append(j)
        else :
            if stack[-1] == j :
                stack.pop()
            else :
                stack.append(j)
    if len(stack) == 0 :
        cnt += 1
print(cnt)