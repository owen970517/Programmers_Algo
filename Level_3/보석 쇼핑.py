def solution(gems) :
    answer = []
    type = set(gems)
    ans = []
    dis = []
    print(type)
    for start in range(len(gems)):
        # end를 가능한 만큼 이동시키기
        print(start)
        end = 0
        while end < len(gems):
            now = gems[start:end+1]
            end += 1
            print(now,set(now))
            if set(now) == type :
                ans.append([start+1,end])
    print(ans)
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))