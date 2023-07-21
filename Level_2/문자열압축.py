def solution(s):
    answer = int(1e9)
    for i in range(1,len(s)+1) :
        lst = [s[j:j+i] for j in range(0, len(s), i)]
        new = ''
        cnt = 1
        for k in range(len(lst)-1) :
            if lst[k] == lst[k+1] :
                cnt += 1
            else :
                if cnt > 1 :
                    new += f'{cnt}{lst[k]}'
                    cnt = 1
                else :
                    new += lst[k]
        if cnt > 1 :
            new += f'{cnt}{lst[-1]}'
        else :
            new += lst[-1]
            
        answer = min(answer,len(new))
    return answer

s = "xababcdcdababcdcd"
print(solution(s))



""" def solution(s):
    answer = []
    li=[]
    for i in range(1, len(s)+1): # i자씩 끊기!
            b = ''
            cnt = 1 #갯수 체크
            tmp=s[:i] # 첫번째 미리 자르기
            #['a', 'aa', 'aab', 'aabb', 'aabba', 'aabbac', 'aabbacc', 'aabbaccc']
            for j in range(i, len(s)+i, i): # i부터 끝까지 i단위로 나누어 탐색
            
                if tmp==s[j:i+j]:# 앞과 같으면 
                    cnt+=1 # 카운트
                    
                else: # 아니면
                    if cnt!=1: # 앞에서 중복이 있었다!
                        b = b + str(cnt)+tmp # 글자 만들기
                        li.append(b)
                    else:
                        b = b + tmp
                        li.append(b)
                    tmp=s[j:j+i]
                    cnt = 1
            answer.append(len(b))
    return min(answer) , li """