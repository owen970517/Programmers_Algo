n = int(input())
for i in range(n) :
    T = int(input())
    li = []
    arr = []
    for j in range(T) :
        k = input()
        li.append(k)
    for i in range(len(li)) :
        for j in range(len(li)) :
            if i != j :
                new = li[i] + li[j]
                re_new = new[::-1] 
                if new == re_new :
                    arr.append(new)
    if len(arr) > 0 :
        print(arr[0])
    else :
        print(0)