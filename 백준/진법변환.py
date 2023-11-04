n, b = input().split()
b = int(b)
n = list(n)
total = 0

for i in range(len(n)):
    if '0' <= n[i] <= '9':  
        k = int(n[i])
    else:  
        k = 10 + ord(n[i]) - ord('A')
    total += k * (b ** (len(n) - (i + 1)))
print(total)