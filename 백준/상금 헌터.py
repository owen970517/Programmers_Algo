t = int(input())
dic1 = {
    500 : [1],
    300 : [2,3],
    200 : [4,5,6],
    50 : [7,8,9,10],
    30 : [11,12,13,14,15],
    10 : [16,17,18,19,20,21]
}
dic2 = {
    512 : [1],
    256 : [2,3],
    128 : [i for i in range(4,8)],
    64 : [i for i in range(8,16)],
    32 : [i for i in range(16,32)],
}
for _ in range(t) :
    total = 0
    a,b = map(int,input().split())
    for i in dic1 :
        if a in dic1[i] :
            total += i
    for j in dic2 :
        if b in dic2[j] :
            total += j
    print(total * 10000)
