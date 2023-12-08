n = int(input())
dic = {
    'b' : 'd',
    'd' : 'b',
    'q' : 'p',
    'z' : 's',
    'i' : 'i',
    'l' : 'l',
    'm' : 'm',
    'n' : 'n',
    'o' : 'o',
    'p' : 'q',
    's' : 'z',
    'u' : 'u',
    'v' : 'v',
    'w' : 'w',
    'x' : 'x'
}
for i in range(n) :
    s = input()
    mirror = []
    isMirror = True
    for j in s :
        if j in dic :
            now = dic[j]
            mirror.append(now)
        else :
            isMirror = False
            break
    mirror_s = ''.join(mirror)
    if s == mirror_s[::-1] and isMirror:
        print('Mirror')
    else :
        print('Normal')