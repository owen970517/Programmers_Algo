s = input()
dic = dict()
length = len(s)
for i in s :
    if i not in dic :
        dic[i] = 1
    else :
        dic[i] += 1
keys = sorted(dic.keys())
cnt = 0
mid = ''
for i in keys :
    if dic[i] %2 == 1 :
        cnt += 1
        if cnt > 1 :
            print("I'm Sorry Hansoo")
            exit()
k = ''
for i in range(length // 2) :
    if dic[keys[i]] % 2 == 0 :
        k += keys[i]
    elif i > len(keys) :
        k += keys[0]
    else :
        mid += keys[i] 
        k += keys[0]
k = sorted(list(k))
k = ''.join(k)
if len(s) % 2 == 0 :
    print(k + k[::-1])
else :
    print(k + mid + k[::-1])