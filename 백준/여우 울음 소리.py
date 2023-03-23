T = int(input())
for _ in range(T):
    recode = list(input().split())
    while 1:
        sound = input()
        if sound == 'what does the fox say?':
            print(' '.join(recode))
            break
        sound = sound.split()
        while sound[-1] in recode:
            recode.remove(sound[-1])