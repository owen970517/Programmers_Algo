n = int(input())
li = list(map(int,input().split()))

stack = [li[0]]
ans = [0]

for i in range(1,n) :
    ans.append(len(stack))
    while stack :
        if stack[-1] <= li[i] :
            stack.pop()
        else :
            break
    stack.append(li[i])

print(ans)