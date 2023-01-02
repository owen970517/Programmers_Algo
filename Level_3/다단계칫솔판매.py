def solution(enroll, referral, seller, amount):
    # 정답 배열 설정
    answer = [0]*len(enroll)
    idx_list={}
    for idx,name in enumerate(enroll):
        idx_list[name]=idx #idx_list = {"john":0, ....}
    # 이제 인덱스가 있기 때문에 인덱스로 부모 조회가 가능하다.
    # 트리를 아예 새로 짜는 게 아니라 부모를 조회하는 방법만 알면 된다.
    for idx,name in enumerate(seller):
        price=100*amount[idx]
        answer[idx_list[name]]+=price #일단 price를 온전히 더함
    for i in seller :
        print(idx_list[i])
        if referral[idx_list[i]] != '-' :
            divied = answer[idx_list[i]] // 10
            print(divied)
            answer[idx_list[i]] -= divied
            answer[idx_list[referral[idx_list[i]]]] += divied
        else :
            answer[idx_list[i]] -= answer[idx_list[i]] // 10
    return answer , idx_list

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12, 4, 2, 5, 10]))