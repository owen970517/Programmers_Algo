n = int(input())
li = []
for _ in range(n) :
	t,w = map(int,input().split())
	li.append((t,w))

nt = 0
for i in range(n) :
	t,w = li[i][0],li[i][1]
	if i == 0 :
		nt = 	t+w
		print(nt)
	else :
		if nt < t :
			nt = t+w
		else :
			nt = nt+w
		print(nt)