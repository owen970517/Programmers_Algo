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
            dic[value] = [count[idx]]
        else :
            dic[value].append(count[idx])
    for i in dic :
        if len(dic[i]) == 6 :
            total_dic[i] = 0
            for j in range(len(dic[i])) :
                if j <4 :
                    total_dic[i] += dic[i][j]
    mins_li =[k for k,v in total_dic.items() if min(total_dic.values()) == v]
    if len(mins_li) == 1 :
        print(mins_li[0])
    else :
        ans_dic = dict()
        for i in mins_li :
            new = dic[i][4]
            ans_dic[i] = new
        ans_dic = dict(sorted(ans_dic.items(), key=lambda x:x[1]))
        print(list(ans_dic.keys())[0])
