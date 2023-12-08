n = int(input())
gather = ['a', 'e','i','o','u']
for i in range(n) :
    ans = []
    s = list(input())
    for j in s :
        if j.lower() in gather :
            ans.append(j)
    if len(ans) > 0:
        print(''.join(ans))
    else :
        print('???')