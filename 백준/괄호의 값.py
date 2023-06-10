s = list(input())
print(s)
pair = {
    '(' : ')',
    '[' :']'
}
value = {
    '()' : 2,
    '[]' : 3
}
stack = []
li = []
for i in range(len(s)) :
    if s[i] == ')' or s[i] == ']' and not stack :
        print(0)
        break
    if stack and s[i] ==')':
        print(stack)
        print(s[i])
        print(pair[stack[-1]],s[i])
    else :
        stack.append(s[i])
        print(stack)
print(li)

        # if pair[stack[-1]] != s[i] :
        #     print(0)
        #     break
        # else :
        #     k = stack.pop()
        #     now = k + s[i]
        #     print(k)
        #     li.append(value[now])