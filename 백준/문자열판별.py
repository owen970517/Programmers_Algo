s = input()
n = int(input())
li = []
state = False
idx = 1
for i in range(n) :
    word = input()
    li.append(word)
print(li[:2])
if s in li :
    state = True
else :
    for i in range(len(li)) :
        
        for j in range(i+1 , len(li)) :
            print(li[i] , li[j:j+idx])
            idx += 1