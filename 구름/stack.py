n,k = map(int,input().split())
li = []
for i in range(n) :
	now = list(map(str,input().split()))
	if now[0] == 'push'  :
		if len(li) < k :
			li.append(now[1])
		else :
			print('Overflow')
	
	if now[0] == 'pop' :
		if len(li) > k :
			print(li.pop())
		else :
			print('Underflow')
