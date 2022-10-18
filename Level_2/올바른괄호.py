def solution(s) :
    answer =True
    li=[]
    cnt=0
    for i in s :
        if i == '(' or i=='[' or i=='{'  :
            li.append(i)
        else :
            if s[0] == ')' or len(li) !=0 or s[0] ==']' or s[0] =='}'  :
                answer = False
            else :
                li.pop()
        if len(li) >0:
            answer =False
    if (answer) :
        cnt +=1
    print(answer)
    return answer,li,cnt

s="[)(]"
print(solution(s))