
while 1 :
    n = int(input())
    li=[]
    upper_li = []
    for _ in range(n):
        s = input()
        li.append(s)
    for i in li :
        upper_li.append(i.upper())
    sorting_li = sorted(upper_li)
    for i in li :
        if sorting_li[0] == i.upper() :
            print(i)
            break
    if n == 0 :
        break
