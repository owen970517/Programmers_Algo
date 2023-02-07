def solution(s, skip, index):
    answer = ''
    skip = set(ord(w) for w in skip)
    for word in s:
        cnt = index
        word = ord(word)
        while cnt != 0:
            word += 1
            if word > ord('z'):
                word = word - 26
            if word in skip:
                continue
            cnt -= 1
        answer += chr(word)
    return answer

print(solution('aukks' , 'wbqd' , 5))