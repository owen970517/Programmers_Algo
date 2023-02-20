k = int(input())
for i in range(k) :
    dic ={}
    n = int(input())
    one = list(input().split())
    two = list(input().split())
    password = list(input().split())
    for j in two :
        dic[one.index(j)] = password.pop(0)
    sort_dic = sorted(dic.items())
    for k in sort_dic :
        print(k[1],end=' ')
    print()