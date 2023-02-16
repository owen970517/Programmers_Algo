import operator

n,m = map(int,input().split())
li = []
answer=''
sum = 0
for i in range(n) :
    dna = input()
    li.append(dna)
for i in range(m) :
    dic = {'A' : 0 , 'C' :0,'G' : 0,'T' :0}
    for j in range(len(li)) :
        dic[li[j][i]] += 1
    max_value = max(dic.items(), key=operator.itemgetter(1))
    answer += max_value[0]
    dic.pop(max_value[0])
    for i in dic.items() :
        if i[1] > 0 :
            sum += i[1]
print(answer,sum ,sep='\n')
