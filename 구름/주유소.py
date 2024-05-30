n = int(input())
dis = list(map(int,input().split()))
price = list(map(int,input().split()))
total  = 0
min_value = 0 

for i in range(n-1)	:
	if i == 0 :
		min_value = price[i]
		total += min_value * dis[i]
	else :
		if min_value > price[i] :
			min_value = price[i] 
		total += min_value * dis[i]
		
print(total)