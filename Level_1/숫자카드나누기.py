def solution(arrayA,arrayB) :
    answer = 0
    a_cnt = 0
    b_cnt = 0
    li=[]
    def getNum(a,b):
        while b:
            a,b=b,a%b
        return a

    def getGcd(array):
        gcd_num = array[0]
        for i in range(1,len(array)):
            gcd_num = getNum(gcd_num,array[i])
        return gcd_num

    gcdA = getGcd(arrayA)
    gcdB = getGcd(arrayB) 
    for i in arrayB :
        if i % gcdA != 0 :
            a_cnt +=1
    for i in arrayA :
        if i % gcdB != 0 :
            b_cnt +=1
    if a_cnt == len(arrayB) :
        li.append(gcdA)
    if b_cnt ==len(arrayB) :
        li.append(gcdB)
    if len(li) > 0 :
        answer = max(li)
    else :
        answer = 0
    return answer

print(solution([14, 35, 119],[18, 30, 102]))