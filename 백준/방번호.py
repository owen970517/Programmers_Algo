n = list(map(int,input()))
plastic = [0] * 10

for i in n :
    if i == 6 or i == 9 :
        if plastic[6] <= plastic[9] :
            plastic[6] +=1
        else :
            plastic[9] += 1
    else :
        plastic[i] += 1

print(plastic)
