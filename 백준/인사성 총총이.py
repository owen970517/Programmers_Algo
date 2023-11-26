import sys


n = int(input())
cnt = 0
dic = {}
for i in range(n) :
    s = input()
    if s == 'ENTER' :
        cnt += sum(dic.values())
        dic ={}
    else :
        if s not in dic :
            dic[s] =1
cnt += sum(dic.values())
print(cnt)
