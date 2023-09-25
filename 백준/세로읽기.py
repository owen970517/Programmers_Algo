li = []
answer = ''
ml = 0
for i in range(5) :
    s = list(input())
    ml = max(ml,len(s))
    li.append(s)

for i in range(ml) :
    for j in range(5) :
        try :
            answer += li[j][i]
        except IndexError:
            continue
print(answer)