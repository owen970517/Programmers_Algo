n = int(input())
word = list(input())

for i in range(n-1) :
    now = input()

    for j in range(len(word)) :
        if word[j] != now[j] :
            word[j] = '?'

print(''.join(word))