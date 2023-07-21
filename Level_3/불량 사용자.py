from itertools import permutations

def solution(user_id,banned_id) :
    answer = 0
    li = []
    star = []
    nCr = list(permutations(user_id,len(banned_id)))
    for i in banned_id :
        l = [i for i, ch in enumerate(i) if ch == '*']
        star.append(l)
    for i in nCr :
        i = list(i)
        new = []
        for j in range(len(i)) :
            re_i = i[j]            
            for k in star[j] :
                if len(i[j])-1 >= max(star[j]) :
                    re_i = re_i.replace(i[j][k],'*')
            new.append(re_i)
        print(new)
        if new == banned_id :
            i = set(i)
            if i not in li :
                li.append(i)
    answer = len(li)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))