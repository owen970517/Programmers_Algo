from itertools import permutations
import re


def solution(user_id, banned_id):
    answer = []
    for perm in permutations(user_id, len(banned_id)):
        banned_perm = []
        for i in range(len(banned_id)):
            banned = banned_id[i].replace('*', '.')
            if re.fullmatch(banned, perm[i]):
                banned_perm.append(perm[i])
        print(banned_perm)
        if len(banned_perm) == len(banned_id):
            banned_perm = set(banned_perm)
            if banned_perm not in answer:
                answer.append(banned_perm)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))