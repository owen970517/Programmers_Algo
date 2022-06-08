def solution(id_list, report, k):
    answer = []
    reporting = {id: [] for id in id_list}
    reports={id: 0 for id in id_list}
    stop=[]
    report = list(set(report))
    for i in report:
        reported=i.split(' ')
        #사람마다 신고 당한 횟수
        reports[reported[1]] +=1
        # 사람마다 신고한 사람
        reporting[reported[0]].append(reported[1])
    # 한 사람이 동일한 사람을 신고했을 경우 1번 취급하니깐 set을 사용
    for i in id_list :
        if reports[i] >= k:
            stop.append(i)
    for i in id_list :
        count =0
        for j in reporting[i]:
            if j in stop:
                count +=1
        answer.append(count) 
    return answer

id_list=["muzi", "frodo", "apeach", "neo"]
report =["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
print(solution(id_list , report,k))