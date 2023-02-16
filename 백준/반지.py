ring = input()
n = int(input())
cnt =0
for _ in range(n) :
    ring_str = input()
    for i in range(len(ring_str)) :
        if ring_str[i:i+len(ring)] == ring :
            cnt += 1
            break 
        if len(ring_str[i:i+len(ring)]) < len(ring) :   
            idx = len(ring) - len(ring_str[i:i+len(ring)])
            now = ring_str[i:i+len(ring)] + ring_str[:idx]
            if now == ring :
                cnt += 1
                break
print(cnt)