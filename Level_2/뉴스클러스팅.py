def solution(str1, str2):
    answer = 0
    # 대소문자 구분안하기 위해 원소를 대문자로 변경
    str1= str1.upper()
    str2 = str2.upper()
    a_li = []
    b_li=[]
    anb=[]
    # 두 글자씩 끊어서 집합 생성
    for i in range(len(str1)-1) :
        if str1[i:i+2].isalpha() :
            a_li.append(str1[i:i+2])
    for i in range(len(str2)-1) :
        if str2[i:i+2].isalpha() :
            b_li.append(str2[i:i+2])
    a_copy = a_li.copy()
    a2 = a_li.copy()
    aub = a_li.copy()
    for i in b_li :
        if i in a2 :
            a2.remove(i)
            anb.append(i)
    for i in b_li :
        if i not in a_copy :
            aub.append(i)
        else :
            a_copy.remove(i)
    if len(anb) == 0 and len(aub) == 0 :
        answer = int(1 * 65536)
    else :
        answer = int(len(anb)/ len(aub) * 65536)
    return answer
    #,str1,str2,a_li,b_li,anb,aub

A = 'aa1+aa2'
B ='AAAA12'
print(solution(A,B))