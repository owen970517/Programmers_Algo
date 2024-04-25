def getPrimeList(n):
    sieve = [False, False] + [True] * (n-1)
    primes = []
    
    for i in range(2, n+1):
        if sieve[i]:          
            primes.append(i)  
            
        for j in range(i*2, n+1, i): 
            sieve[j] = False         

    return primes

n=int(input())
li = getPrimeList(n)
start = 0
end = 0
total = 0
ans = 0
while start <= len(li)-1 and end <= len(li)-1:
    if total == n :
        ans += 1
        total -= li[start]
        start += 1
    else :

        if total < n :
            total += li[end]
            end += 1
        else :
            total -= li[start]
            start += 1
if n in li :
    print(ans+1)
else :
    print(ans)