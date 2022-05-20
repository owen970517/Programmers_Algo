def solution(id_list, report, k):
    answer = [0]* len(id_list)
    reporting = {id: [] for id in id_list}
    reports=[]
    cnt=[]
    for i in report:
        reported=i.split(' ')
        #신고 당한 사람 
        reports.append(reported[1])
        reporting[reported[0]].append(reported[1])
    for i in reporting:
        print(i)
    return answer,reporting,reports,cnt

id_list=["muzi", "frodo", "apeach", "neo"]
report =["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
print(solution(id_list , report,k))