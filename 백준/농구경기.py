n = int(input())
dic = dict()
answer = ''
for i in range(n) :
    s = input()
    if s[0] not in dic :
        dic[s[0]] = 1
    else :
        dic[s[0]] += 1
dic = dict(sorted(dic.items()))
for i in dic :
    if dic[i] >= 5 :
        answer += i
if answer == '' :
    print('PREDAJA')
else :
    print(answer)