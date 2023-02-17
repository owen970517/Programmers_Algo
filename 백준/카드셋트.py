s = input()
dic = {'P' : 0 ,'K' : 0 , 'H' : 0,'T' :0}
num = []
for i in range(len(s)//3) :
    card = s[i*3:i*3+3]
    shape = card[0]
    dic[shape] += 1
    num.append((shape,card[1:3]))
li = list(dic.items())
if len(set(num)) != len(num) :
    print("GRESKA")
else :
    for i in range(len(li)) :
        print(13-int(li[i][1]),end=' ')
