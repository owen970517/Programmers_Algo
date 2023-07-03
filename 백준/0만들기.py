from copy import deepcopy

def bt(now) :
    if len(now) == n-1 :
        op.append(deepcopy(now))
        return
    now.append(' ')
    bt(now)
    now.pop()

    now.append('+')
    bt(now)
    now.pop()

    now.append('-')
    bt(now)
    now.pop()

t=  int(input())
for i in range(t) :
    op = []
    n = int(input())
    li = [i for i in range(1,n+1)]
    bt([])
    now = ''
    for i in op :
        temp = ""
        for j in range(1, n):
            temp += str(j) + str(i[j - 1])
        temp += str(n)   
        if eval(temp.replace(' ','')) == 0 :
            print(temp)
    print()