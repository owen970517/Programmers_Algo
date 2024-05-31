n = int(input())
p = list(map(int, input().split()))
dic = {}

for _ in range(n):
    d, t = map(int, input().split())
    if d not in dic:
        dic[d] = [t]
    else:
        dic[d].append(t)

sorted_dic = {k: sorted(v) for k, v in dic.items()}
sorted_dic = sorted(sorted_dic.items(), key=lambda x: x[0])

total = 0
for idx, (diff, times) in enumerate(sorted_dic):
    times = times[:p[diff-1]]  
    total += sum(times)  
    if len(times) > 1:  
        rest_times = [times[i] - times[i-1] for i in range(1, len(times))]
        total += sum(rest_times) 
    if idx < len(p)-1:  
        total += 60

print(total)