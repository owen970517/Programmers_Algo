n = int(input())
li = list(map(int,input().split()))
goal = sorted(li)
temp = []

while li :
    if li[0] == goal[0] :
        li.pop(0)
        goal.pop(0)
    else :
        temp.append(li.pop(0))
    if temp :
        while temp :
            if temp[-1] == goal[0] :
                temp.pop()
                goal.pop(0)
            else :
                break
        
if not temp and not goal :
    print('Nice')
else :
    print('Sad')

    

