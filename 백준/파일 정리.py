n = int(input())
dic={}
for i in range(n) :
    a,b = map(str,input().split('.'))
    if b not in dic :
        dic[b] = 1
    else :
        dic[b] += 1
sort_dic = sorted(dic.items())
for i in range(len(dic)):
    print(sort_dic[i][0],sort_dic[i][1])
