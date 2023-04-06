import itertools
def solution(n,m,names,authors) :
    answer = 0
    dic = dict()
    for i in authors :
        if 'erdos' in i  :
            for j in range(len(i)) :
                if i[j] != 'erdos' :
                    dic[i[j]] = 1
                else :
                    dic[i[j]] = 0
        else :
            for j in range(len(i)) :
                if i[j] in dic :
                    dic[i[j+1]] = dic[i[j]] +1
                    break
        all =0
        for k in range(2,len(dic)) :
            nPr = list(itertools.permutations(dic,k))
            aa= 0 
            for i in nPr :
                sum = 0
                for j in range(len(i)) :
                    sum += dic[i[j]]
                if sum <= 6 :
                    aa += 1
            all += aa
        print(all)
    return answer,dic
print(solution(8,8,
            ["justi","cehui","jhnah","erdos","aaaaa","bbbbb","ccccc","ddddd"],
            [["erdos","justi"],["justi","cehui"],["cehui","jhnah"],["jhnah","aaaaa"],["aaaaa","bbbbb"],["bbbbb","ccccc"],["ccccc","ddddd"],["ccccc","ddddd"]]))