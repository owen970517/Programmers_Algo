s = input()
li =[]
for i in range(len(s)) :
    for j in range(i+1,len(s)+1) :
        print(s[i:j])
        li.append(s[i:j])

print(len(list(set(li))))