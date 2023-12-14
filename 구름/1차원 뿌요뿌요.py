n,m = map(int,input().split())
li = list(input())
print(li)
stack = [li[0]]
cnt = 1
for i in range(1,n) :
    print(stack,i,cnt)
    now = li[i]
    while stack :
        if stack[-1] == now :
            cnt += 1            
            stack.append(now)
            break
        else :
            if cnt >= m :
                for _ in range(cnt) :
                    stack.pop()
                print(stack)
            now = li[i]
            cnt = 1
            
print(stack)