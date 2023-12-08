n,m = map(int, input().split())
li = list(map(int, input().split()))
start, end = 0, max(li)+(m//n)
while start <= end:
	mid = (start + end) // 2
	print(start,end)
	now = 0 
	for i in li:
		if i < mid:
			now += (mid - i)
	if now <= m :
		start = mid + 1
	else :
		end = mid -1
now = 0
for i in li:
	if i < mid:
		now += (mid - i)

if now <= m :
	print(end)
else :
	print('No way!')