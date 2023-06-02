t = int(input())
for i in range(t) :
    n = int(input())
    dic = dict()
    total_dic = dict()
    li = list(map(int,input().split()))  
    count = []
    for i in range(len(li)) :   
        if li.count(li[i]) >= 6 :
            k = count.count(0)
            count.append(i+1-k)
        else :
            count.append(0)
    for idx,value in enumerate(li) :
        if value not in dic :
            dic[value] = [idx]
        else :
            dic[value].append(idx)
    print(dic)
    for i in dic :
        if len(dic[i]) >= 6 :
            total_dic[i] = 0
            for j in range(len(dic[i])) :
                if j <4 :
                    total_dic[i] += count[dic[i][j]]
                    
    print(list(total_dic.items()))
    total_dic = list(sorted(total_dic.items(),key=lambda x:x[1]))
    print(min(total_dic))
