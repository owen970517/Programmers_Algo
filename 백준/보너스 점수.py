n = int(input())
li = list(input())
total = 0
bonus = 0

for i in range(n) :
    if li[i] == 'O' :
        total += (i+1)
        total += bonus
        bonus += 1
    else :
        bonus = 0 
print(total)