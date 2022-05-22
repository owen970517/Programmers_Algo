def solution(answers):
    answer = []
    first_cnt,sec_cnt,thr_cnt=0,0,0
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == a1[i%len(a1)] :
            first_cnt+=1
        if answers[i] == a2[i%len(a2)]:
            sec_cnt +=1
        if answers[i] == a3[i%len(a3)]:
            thr_cnt+=1
        
    max_cnt = max(first_cnt,sec_cnt,thr_cnt)
    if max_cnt == first_cnt:
        answer.append(1)
    if max_cnt == sec_cnt:
        answer.append(2)
    if max_cnt == thr_cnt:
        answer.append(3)
    return answer

answers = [1,3,2,4,2]	
print(solution(answers))