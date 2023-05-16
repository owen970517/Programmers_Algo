s = list(input())
dic = dict()
for i in range(97,123) :
    dic[chr(i)] = 0
for i in s :
    dic[i] += 1

for i in dic :
    print(dic[i],end=' ')