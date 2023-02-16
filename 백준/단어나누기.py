s = list(input())
li = []
for i in range(1,len(s)-1) :
    for j in range(i,len(s)-1) :
        first = s[:i]
        second = s[i:j+1]
        third =s[j+1::]
        first.reverse()
        second.reverse()
        third.reverse()
        new_s = first+second+third
        li.append(''.join(new_s))
li.sort()
print(li[0])