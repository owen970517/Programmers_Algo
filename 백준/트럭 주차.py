a,b,c = map(int,input().split())
arr = [0] * 100 
price = 0
for _ in range(3) :
    start,end = map(int,input().split())
    for i in range(start,end) :
        arr[i] += 1
for i in range(1,len(arr)) :
    if arr[i] == 1 :
        price += arr[i] * a
    elif arr[i] == 2 :
        price += arr[i] * b
    elif arr[i] == 3 :
        price += arr[i] * c
print(price)