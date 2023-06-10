t = int(input())
for i in range(t) :
    n = int(input())
    binary = list(bin(n))[2:]
    ans = []
    binary = list(reversed(binary))
    for idx,value in enumerate(binary) :
        if value == '1' :
            ans.append(idx)
    print(*ans) 