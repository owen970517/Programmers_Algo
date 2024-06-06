import sys
n = int(input())
li = []
for i in range(n) :
    s = input()
    li.append(s)
words = {}
for s in li: 
    x = len(s)-1
    for i in s :
        if i in words:
            words[i] += 10**x
        else :
            words[i] = 10**x
        x -= 1

words_sort = sorted(words.values(),reverse=True)

now = 9
ans = 0

for i in words_sort :
    ans += now * i
    now -= 1
print(ans)