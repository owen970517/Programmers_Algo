N = int(input())

WordSet = set()

 

def check(word):

    global WordSet

 

    wordLen = len(word)

    for src in WordSet:

        if len(src) != wordLen:

            continue

 

        for i in range(wordLen):

            if src == word:

                return True

            

            word = f"{word[1:]}{word[0]}"
    return False

for i in range(N):

    word = input()

    if not check(word):
        print(word)
        WordSet.add(word)
print(WordSet)
print(len(WordSet))