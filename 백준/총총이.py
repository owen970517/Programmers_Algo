n = int(input())
rainbowdance = []
for i in range(n) :
    now = input().split()
    if 'ChongChong' in now :
        rainbowdance.append(now[0])
        rainbowdance.append(now[1])
    elif now[0] in rainbowdance :
        rainbowdance.append(now[1])
    elif now[1] in rainbowdance :
        rainbowdance.append(now[0])
print(len(list(set(rainbowdance))))
