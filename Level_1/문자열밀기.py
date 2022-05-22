def solution(s, n):
    answer = ''
    li=[]
    for i in range(len(s)):
        if s[i] == " ":
            li.append(32)
        if s[i].isupper():
            li.append((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            li.append((ord(s[i])-ord('a')+ n)%26+ord('a'))
    for i in li:
        answer += chr(i)
    return answer

s = "a B z"
n = 4
print(solution(s,n))