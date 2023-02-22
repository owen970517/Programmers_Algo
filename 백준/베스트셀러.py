n = int(input())
dic = {}
li = []
for i in range(n) :
    s = input()
    if s not in dic :
        dic[s] = 1
    else :
        dic[s] += 1
max_value = max(dic.values())
sorted_dic = dict(sorted(dic.items() , key=lambda x:(x[1]) , reverse=True))
for i in sorted_dic :
    if sorted_dic[i] == max_value :
        li.append(i)
li.sort()
print(li[0])