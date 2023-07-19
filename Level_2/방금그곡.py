from math import ceil

def change(k) :
    k = k.split(':')
    h = int(k[0])* 60 + int(k[1])
    return h

def solution(m,musicinfos) :
    answer = '(None)'
    arr =[]
    dic = {
        'C#':'c',
        'D#' : 'd',
        'F#' :'f',
        'G#' :'g',
        'A#' :'a'
    }
    for key, value in dic.items():
        m = m.replace(key, value)

    for i in musicinfos :
        li = i.split(',')
        l=change(li[0])
        r=change(li[1])
        song = li[2]
        info = li[3]
        elapsed = r-l
        for key, value in dic.items():
            info = info.replace(key, value)
        if elapsed > len(info) :
            repeat = ceil(elapsed/len(info))
            now = info * repeat
        else :
            now= info[:elapsed]
        if m in now :
            arr.append([elapsed,song])      
    arr.sort(key=lambda x:x[0], reverse=True )
    if len(arr) > 0 :
        answer = arr[0][1]

    return answer

print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))