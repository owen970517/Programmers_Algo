li = []
n = input()
m = input()
li.append(n)
li.append(m)
s=''
sign = {'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50,'C' : 100 , 'D' : 500,'M' : 1000 , 'IV' : 4 , 'IX' : 9 , 'XL' : 40 , 'XC' : 90,'CD' : 400,'CM' : 900} 
total = 0

for i in range(len(li)) :
    sum = 0
    visited = [0]* len(li[i]) 
    for j in range(len(li[i])) :
        if visited[j] == 0 :
            if j < len(li[i])-1 and sign[li[i][j]] >= sign[li[i][j+1]] or j == len(li[i]) -1  :
                visited[j]= 1
                sum += sign[li[i][j]]
            else :
                visited[j] , visited[j+1] = 1,1
                now = li[i][j] + li[i][j+1]
                sum += sign[now]
    total += sum
print(total)
while total > 0 :
    if total >= 1000 :
        total -= 1000
        s += 'M'
    elif total >= 900 :
        total -= 900 
        s += 'CM'
    elif total >= 500 :
        total-=500
        s +='D'
    elif total >= 400 :
        total -=400
        s +='CD'
    elif total >= 100 :
        total -= 100
        s += 'C'
    elif total >= 90 :
        total -= 90
        s +='XC'
    elif total >= 50 :
        total-=50
        s +='L'
    elif total >= 40 :
        total -= 40
        s+='XL'
    elif total >= 10 :
        total -= 10 
        s += 'X'
    elif total >= 9 :
        total -= 9
        s +='IX'
    elif total >= 5 :
        total -= 5
        s +='V'
    elif total >= 4 :
        total -=4 
        s +='IV'
    else :
        total -= 1 
        s += 'I'

print(s)
        